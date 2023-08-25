import ocr
import models

file_name = "medicalese/Sample Report.png"

if __name__ == "__main__":
    # print(ocr.image_report(file_name))
    print(models.bio_summarize(file_name))