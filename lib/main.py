import ocr
import bio_summarize as bio_summarize
from explainer import explainer

import warnings
warnings.filterwarnings("ignore")

file_name = "lib/Sample Report.png"

if __name__ == "__main__":
    report_summary = bio_summarize.bio_summarize(file_name)
    print(explainer(report_summary))