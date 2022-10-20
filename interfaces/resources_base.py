from abc import ABC, abstractmethod


class ResourcesBase(ABC):
    @abstractmethod
    def get_processor_percentage_usage(self):
        """Pobiera procentową wartość zużycia procesora"""

    @abstractmethod
    def get_ram_percentage_usage(self):
        """Pobiera procentową wartość zużycia RAMu"""

    @abstractmethod
    def get_network_usage(self):
        """Pobiera aktualne zużycie sieci"""

    @abstractmethod
    def get_disk_capacity(self):
        """Pobiera całkowitą pojemność dysku"""

    @abstractmethod
    def get_disk_usage(self):
        """Pobiera aktualną zajętość dysku"""