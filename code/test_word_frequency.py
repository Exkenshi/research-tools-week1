# 词频统计程序测试脚本

import subprocess
import os
import sys


def run_test_case(test_name, command, expected_keywords=None):
    """运行单个测试用例"""
    print(f"\n=== {test_name} ===")
    print(f"命令: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
        
        print(f"返回码: {result.returncode}")
        print("\n输出:")
        print(result.stdout)
        
        if result.stderr:
            print("\n错误信息:")
            print(result.stderr)
        
        # 检查预期关键词是否在输出中
        if expected_keywords:
            all_found = True
            for keyword in expected_keywords:
                if keyword.lower() not in result.stdout.lower():
                    all_found = False
                    print(f"警告: 预期关键词 '{keyword}' 未在输出中找到")
            
            if all_found:
                print("✓ 所有预期关键词都找到了")
            else:
                print("✗ 部分预期关键词未找到")
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"运行测试时发生错误: {e}")
        return False


def create_larger_test_file():
    """创建更大的测试文件"""
    print("\n=== 创建更大的测试文件 ===")
    
    # 生成重复的文本内容
    words = ["python", "programming", "data", "analysis", "security", "privacy", 
             "algorithm", "machine", "learning", "artificial", "intelligence", 
             "computer", "science", "technology", "software", "development"]
    
    sentences = [
        "Python is a popular programming language for data analysis.",
        "Data security and privacy protection are important topics.",
        "Machine learning algorithms can help in pattern recognition.",
        "Artificial intelligence is transforming technology.",
        "Computer science education is essential for software development.",
        "Privacy protection requires careful algorithm design.",
        "Data analysis helps in making informed decisions.",
        "Programming skills are fundamental in technology.",
        "Security measures must be implemented in software development.",
        "Learning algorithms improves problem-solving abilities."
    ]
    
    # 创建更大的文件
    content = []
    for i in range(20):  # 重复20次
        for sentence in sentences:
            content.append(sentence)
    
    # 添加一些重复的词
    for word in words:
        content.extend([word] * 10)  # 每个词重复10次
    
    with open("large_test.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    
    print("已创建 large_test.txt 文件")
    return "large_test.txt"


def main():
    print("词频统计程序测试开始")
    print("=" * 50)
    
    # 检查程序文件是否存在
    if not os.path.exists("word_frequency.py"):
        print("错误: word_frequency.py 文件不存在")
        return
    
    # 测试1: 基本功能测试
    run_test_case(
        "基本功能测试",
        "python word_frequency.py test.txt",
        ["hello", "world", "python", "programming"]
    )
    
    # 测试2: 指定输出文件
    run_test_case(
        "输出文件测试",
        "python word_frequency.py test.txt -o result.txt",
        ["结果已保存到"]
    )
    
    # 测试3: 显示前5个高频词
    run_test_case(
        "前5个高频词测试",
        "python word_frequency.py test.txt -n 5",
        ["出现频率最高的前 5 个词"]
    )
    
    # 测试4: 保存所有结果
    run_test_case(
        "保存所有结果测试",
        "python word_frequency.py test.txt -o all_results.txt --save-all",
        ["结果已保存到"]
    )
    
    # 测试5: 测试不存在的文件
    run_test_case(
        "错误处理测试",
        "python word_frequency.py nonexistent.txt",
        ["错误", "不存在"]
    )
    
    # 创建更大的测试文件并进行测试
    large_file = create_larger_test_file()
    
    # 测试6: 大文件测试
    run_test_case(
        "大文件测试",
        f"python word_frequency.py {large_file} -n 10",
        ["总词数", "不同词数", "出现频率最高的前 10 个词"]
    )
    
    print("\n" + "=" * 50)
    print("测试完成!")
    print("\n使用说明:")
    print("1. 基本用法: python word_frequency.py <文件名>")
    print("2. 指定输出: python word_frequency.py <文件名> -o <输出文件>")
    print("3. 显示前N个: python word_frequency.py <文件名> -n <数量>")
    print("4. 保存所有结果: python word_frequency.py <文件名> -o <输出文件> --save-all")
    
    print("\n测试文件说明:")
    print("- test.txt: 基本测试文件")
    print("- large_test.txt: 大型测试文件（用于性能测试）")
    print("- result.txt: 基本测试结果")
    print("- all_results.txt: 所有词频结果")


if __name__ == "__main__":
    main()
