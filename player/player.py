import argparse
from typing import NoReturn

from .network.client import Client
from .player_logic.next_actions import get_next_actions

#ville 
class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int, username: str
    ) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []

    def run(self: "PlayerGameClient") -> NoReturn:
        while True:
            game_data = self.read_json()

            commands = get_next_actions(game_data, self.username)
            for command in commands:
                self.add_command(command)

            self.send_commands()

    def add_command(self: "PlayerGameClient", command: str) -> None:
        self._commands.append(command)

    def send_commands(self: "PlayerGameClient") -> None:
        data = {"commands": self._commands}
        print("sending", data)
        self.send_json(data)
        self._commands.clear()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game client.")
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        help="name of server on the network",
        default="localhost",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help="location where server listens",
        default=1271,
    )
    parser.add_argument(
        "-u",
        "--username",
        type=str,
        help="name of the user",
        default="AgricultorSimulator"
    )
    args = parser.parse_args()

    client = PlayerGameClient(args.address, args.port, args.username).run()
