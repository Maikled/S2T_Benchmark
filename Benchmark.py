from os import path
from Data.Calculations import calculate_wer
from Data.Convertions import convert_string
import datetime


def run(model, data_manager):
    data = data_manager.load_data()
    model.load()

    model_file_stats = model.model_name + ".txt"
    data_manager.save_results_data(model_file_stats, f"Model\tWER\tTarget\tResult\tTime,sec")

    total_spend_time = datetime.timedelta()
    wer_all = 0
    for elem in data:
        start_time = datetime.datetime.now()
        result = model.transcribe(path.join(data_manager.path_to_audio_folder, elem.audio_file_name))
        end_time = datetime.datetime.now()
        spend_time = end_time - start_time
        total_spend_time += spend_time

        result_string = convert_string(result)
        target_string = convert_string(elem.target_text)

        wer = calculate_wer(target_string, result_string)
        wer_all += wer

        stats_string = f"{model.model_name}\t{wer * 100}\t{target_string}\t{result_string}\t{spend_time.total_seconds()}"
        data_manager.save_results_data(model_file_stats, stats_string)
        print(stats_string)

    avg_wer = wer_all / len(data)
    final_stats_wer_string = f"Total WER: {model.model_name}\t{avg_wer * 100}"
    final_stats_time_string = f"Total spend time: {model.model_name}\t{total_spend_time}"
    data_manager.save_results_data(model_file_stats, final_stats_wer_string)
    data_manager.save_results_data(model_file_stats, final_stats_time_string)
    print(final_stats_wer_string)
    print(final_stats_time_string)
