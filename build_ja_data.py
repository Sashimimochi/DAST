import argparse
from databuilder.data_processor import DataProcessor
from databuilder.make_ja_dataset import MakeJaDataset
import yaml

with open('./databuilder/params.yml') as f:
    params = yaml.safe_load(f)

POSITIVE_REVIEW_STARS_LIMIT = params['POSITIVE_REVIEW_STARS_LIMIT']
NEGATIVE_REVIEW_STARS_LIMIT = params['NEGATIVE_REVIEW_STARS_LIMIT']
NUM_OF_SENTENCES_LIMIT = params['NUM_OF_SENTENCES_LIMIT']
MIN_NUM_OF_WORDS_LIMIT = params['MIN_NUM_OF_WORDS_LIMIT']
MAX_NUM_OF_WORDS_LIMIT = params['MAX_NUM_OF_WORDS_LIMIT']
TEST_SIZE = params['TEST_SIZE']
VALIDATION_SIZE = params['VALIDATION_SIZE']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--positive_review_stars_limit",
                        type=int,
                        default=POSITIVE_REVIEW_STARS_LIMIT,
                        help="limit for positive reviews"
                        )
    parser.add_argument("--negative_review_stars_limit",
                        type=int,
                        default=NEGATIVE_REVIEW_STARS_LIMIT,
                        help="limit for negative reviews"
                        )
    parser.add_argument("--num_of_sentences_limit",
                        type=int,
                        default=NUM_OF_SENTENCES_LIMIT,
                        help="limit for the number of sentences in the review"
                        )
    parser.add_argument("--min_num_of_words_limit",
                        type=int,
                        default=MIN_NUM_OF_WORDS_LIMIT,
                        help="limit for the minimum number of word in the review"
                        )
    parser.add_argument("--max_num_of_words_limit",
                        type=int,
                        default=MAX_NUM_OF_WORDS_LIMIT,
                        help="limit for the maximum number of word in the review"
                        )
    parser.add_argument("--test_size",
                        type=float,
                        default=TEST_SIZE,
                        help="test set size"
                        )
    parser.add_argument("--validation_size",
                        type=float,
                        default=VALIDATION_SIZE,
                        help="validation set size"
                        )
    parser.add_argument("--dataset_path",
                        type=str,
                        default="data/tmp/mydata.json",
                        help="path of the dataset"
                        )
    parser.add_argument("--lang",
                        type=str,
                        default="ja",
                        help="language"
                        )

    opt = parser.parse_args()

    MakeJaDataset().build_ja_data()

    data_processor = DataProcessor(
        opt.positive_review_stars_limit,
        opt.negative_review_stars_limit,
        opt.num_of_sentences_limit,
        opt.min_num_of_words_limit,
        opt.max_num_of_words_limit,
        opt.test_size,
        opt.validation_size,
        opt.lang
    )
    data_processor.process_data(opt.dataset_path)
    data_processor.concat_data()


if __name__ == "__main__":
    main()
