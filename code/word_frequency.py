import re
import string
from collections import Counter
import argparse
import sys


def read_text_file(file_path):
    """读取文本文件"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return None
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        return None


def preprocess_text(text):
    """文本预处理"""
    # 转换为小写
    text = text.lower()
    # 移除标点符号
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    # 移除数字
    text = re.sub(r"\d+", "", text)
    # 移除多余的空白字符
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_text(text):
    """分词"""
    words = text.split()
    return words


def count_word_frequency(words):
    """统计词频"""
    word_counts = Counter(words)
    return word_counts


def get_top_words(word_counts, top_n=10):
    """获取出现频率最高的前N个词"""
    return word_counts.most_common(top_n)


def print_word_frequency(word_counts, top_n=None):
    """打印词频统计结果"""
    if top_n:
        top_words = get_top_words(word_counts, top_n)
        print(f"\n出现频率最高的前 {top_n} 个词：")
        print("-" * 50)
        for word, count in top_words:
            print(f"{word:<15} {count:>5}")
    else:
        print("\n所有词的频率统计：")
        print("-" * 50)
        for word, count in word_counts.most_common():
            print(f"{word:<15} {count:>5}")


def save_results(word_counts, output_file=None, top_n=50):
    """保存结果到文件"""
    if not output_file:
        return
    
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("词频统计结果\n")
            file.write("=" * 50 + "\n")
            for word, count in get_top_words(word_counts, top_n):
                file.write(f"{word}\t{count}\n")
        print(f"结果已保存到：{output_file}")
    except Exception as e:
        print(f"保存结果时发生错误：{e}")


def main():
    parser = argparse.ArgumentParser(description="文本词频统计程序")
    parser.add_argument("input_file", help="输入文本文件路径")
    parser.add_argument("-o", "--output", help="输出文件路径")
    parser.add_argument("-n", "--top", type=int, default=10, 
                       help="显示前N个高频词（默认10）")
    parser.add_argument("--save-all", action="store_true",
                       help="保存所有词频结果")
    
    args = parser.parse_args()
    
    # 读取文件
    text = read_text_file(args.input_file)
    if text is None:
        return
    
    # 文本预处理
    processed_text = preprocess_text(text)
    
    # 分词
    words = tokenize_text(processed_text)
    
    # 统计词频
    word_counts = count_word_frequency(words)
    
    # 输出结果
    print(f"\n文件：{args.input_file}")
    print(f"总词数：{len(words)}")
    print(f"不同词数：{len(word_counts)}")
    
    print_word_frequency(word_counts, args.top)
    
    # 保存结果
    if args.output:
        save_top_n = args.top if not args.save_all else None
        save_results(word_counts, args.output, save_top_n)


if __name__ == "__main__":
    main()
