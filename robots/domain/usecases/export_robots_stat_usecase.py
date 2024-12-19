from io import BytesIO

import xlsxwriter

from robots.domain.daos.robots_dao import RobotDAO


class ExportRobotsStatUsecase:
    def __init__(self, robot_dao: RobotDAO) -> None:
        self._robot_dao = robot_dao

    def execute(self) -> bytes:
        stat_headers = ["Модель", "Версия", "Количество за неделю"]
        stat_iterable = self._robot_dao.get_counts_grouped_by_model_and_version()
        tmp_buffer = BytesIO()
        workbook = xlsxwriter.Workbook(tmp_buffer, options={})

        idx = 1
        prev_model = None

        for serial_stat in stat_iterable:
            model = serial_stat["model"]

            if model != prev_model:
                worksheet = workbook.add_worksheet(model)

                # ипшем заголовки
                for col_num, col in enumerate(stat_headers):
                    worksheet.write(0, col_num, col)

                # перезапускаем счетчик и предыдущую модель, тк новая страница
                idx = 1
                prev_model = model

            worksheet.write_row(
                idx,
                0,
                [serial_stat["model"], serial_stat["version"], serial_stat["count"]],
            )
            idx += 1

        workbook.close()
        tmp_buffer = tmp_buffer.getvalue()
        return tmp_buffer
