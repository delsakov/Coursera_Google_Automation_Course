#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = []
  empty_line = Spacer(1,20)
  for item in additional_info:
    report_info.append(Paragraph(item[0], styles["BodyText"]))
    report_info.append(empty_line)
  data = [report_title, empty_line]
  data.extend(report_info)
  report.build(data)
