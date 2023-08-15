import pandas as pd


class File:
    """
    File importer

    Contains all functions regarding reading and parsing data from file. Can be expanded to handle output as well.
    """

    @classmethod
    def load(
        cls, filename: str = "satellites.dat", filepath: str = "../dat"
    ) -> pd.DataFrame:
        """
        Loads a .csv into a pandas dataframe with two columns: start and end.
        Currently only supports .csv files with two columns, containing start and end time.

        More adaptive parser has to be implemented to handle multiple different time formats. Currently supported
        datetime format is HH:MM:SS.f

        :param filename: str
        :param filepath: str
        :return: pd.DataFrame
        """
        df = pd.read_csv(
            f"{filepath}/{filename}",
            names=["start", "end"],
            parse_dates=["start", "end"],
            date_format="%H:%M:%S.%f",
        )
        return df
