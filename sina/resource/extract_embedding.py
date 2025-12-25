# extract_embedding.py

# 输入文件：你下载的800万全量文件路径
input_file = "Tencent_AILab_ChineseEmbedding.txt"
# 输出文件：项目需要的50万词文件路径
output_file = "embedding_500000.txt"

limit = 500000

print(f"开始截取前 {limit} 个词向量...")

with open(input_file, 'r', encoding='utf-8', errors='ignore') as f_in:
    # 读取第一行（头信息：包含总词数和维度）
    header = f_in.readline()

    with open(output_file, 'w', encoding='utf-8') as f_out:
        # 写入新的头信息，手动将总数改为 500000
        # 腾讯词向量维度通常是 200
        f_out.write(f"{limit} 200\n")

        # 循环读取并写入前 500000 行
        for i, line in enumerate(f_in):
            if i >= limit:
                break
            f_out.write(line)

            if (i + 1) % 50000 == 0:
                print(f"已处理 {i + 1} 条...")

print("截取完成！请确保 config.json 中的 WORD_EMBEDDING_PATH 指向此生成文件。")