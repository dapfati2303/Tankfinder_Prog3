"""Projekt INformation zum Tankstellenfinder"""


class application:
    def __init__(self, name, version, description, developers, maintainer, tags):
        self.name = name
        self.version = version
        self.description = description
        self.developers = ["Paul Thurner", "Adrian Pfatischer", "Julian Fischer", "Raphael Goester"]
        self.maintainer = "Paul Thurner"
        self.tags = ["tankstellen", "spritpreise", "flask", "leaflet", "pandas", "tankerkoenig", "openstreetmap"]

    def status(self):
        return (f"{self.name} {self.version}: {self.description}\n"
                f"Team: {', '.join(self.developers)} "
                f"(Maintainer: {self.maintainer})\n"
                f"Tags: {', '.join(self.tags)}")


APP = application(
    name="Tankfinder",
    version="0.1.0",
    description="Günstigste Tankstellen im Umkreis finden und Route anzeigen",
    developers=["Paul Thurner", "Adrian Pfatischer", "Julian Fischer", "Raphael Goester"],
    maintainer="Paul Thurner",
    tags=["tankstellen", "spritpreise", "flask", "leaflet", "pandas", "tankerkoenig", "openstreetmap"],
)