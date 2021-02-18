from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Union

from PySide2 import QtGui
from PySide2.QtCore import QItemSelectionModel
from PySide2.QtGui import QStandardItem, QStandardItemModel
from PySide2.QtWidgets import QAbstractItemView, QListView

import qt_ui.uiconstants as CONST
from game.theater import ConflictTheater

PERF_FRIENDLY = 0
PERF_MEDIUM = 1
PERF_HARD = 2
PERF_NASA = 3


@dataclass(frozen=True)
class Campaign:
    name: str
    icon_name: str
    authors: str
    description: str
    recommended_player_faction: str
    recommended_enemy_faction: str
    performance: Union[PERF_FRIENDLY, PERF_MEDIUM, PERF_HARD, PERF_NASA]
    data: Dict[str, Any]
    path: Path

    @classmethod
    def from_json(cls, path: Path) -> Campaign:
        with path.open() as campaign_file:
            data = json.load(campaign_file)

        sanitized_theater = data["theater"].replace(" ", "")
        return cls(
            data["name"],
            f"Terrain_{sanitized_theater}",
            data.get("authors", "???"),
            data.get("description", ""),
            data.get("recommended_player_faction", "USA 2005"),
            data.get("recommended_enemy_faction", "Russia 1990"),
            data.get("performance", 0),
            data,
            path,
        )

    def load_theater(self) -> ConflictTheater:
        return ConflictTheater.from_json(self.path.parent, self.data)


def load_campaigns() -> List[Campaign]:
    campaign_dir = Path("resources\\campaigns")
    campaigns = []
    for path in campaign_dir.glob("*.json"):
        try:
            logging.debug(f"Loading campaign from {path}...")
            campaign = Campaign.from_json(path)
            campaigns.append(campaign)
        except RuntimeError:
            logging.exception(f"Unable to load campaign from {path}")

    return sorted(campaigns, key=lambda x: x.name)


class QCampaignItem(QStandardItem):
    def __init__(self, campaign: Campaign) -> None:
        super(QCampaignItem, self).__init__()
        self.setIcon(QtGui.QIcon(CONST.ICONS[campaign.icon_name]))
        self.setEditable(False)
        self.setText(campaign.name)


class QCampaignList(QListView):
    def __init__(self, campaigns: List[Campaign]) -> None:
        super(QCampaignList, self).__init__()
        self.model = QStandardItemModel(self)
        self.setModel(self.model)
        self.setMinimumWidth(250)
        self.setMinimumHeight(350)
        self.campaigns = []
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.setup_content(campaigns)

    def setup_content(self, campaigns: List[Campaign]) -> None:
        for campaign in campaigns:
            self.campaigns.append(campaign)
            item = QCampaignItem(campaign)
            self.model.appendRow(item)
        self.setSelectedCampaign(0)
        self.repaint()

    def setSelectedCampaign(self, row):
        self.selectionModel().clearSelection()
        index = self.model.index(row, 0)
        if not index.isValid():
            index = self.model.index(0, 0)
        self.selectionModel().setCurrentIndex(index, QItemSelectionModel.Select)
        self.repaint()

    def clear_layout(self):
        self.model.removeRows(0, self.model.rowCount())
