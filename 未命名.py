import random
import time
from dataclasses import dataclass
from typing import List, Dict

# ===================== 数据结构定义（标准化 Agent 间交互） =====================
@dataclass
class Topic:
    """选题数据结构"""
    title: str
    audience: str
    advantage: str
    heat_score: int  # 热度评分 1-10

@dataclass
class ScriptNode:
    """脚本分镜节点"""
    time: str  # 时长
    scene: str  # 镜头
    lines: str  # 台词

@dataclass
class Material:
    """素材推荐"""
    type: str  # 视频/图片/音频
    content: str
    commercial: bool = True  # 是否可商用

@dataclass
class OptimizeAdvice:
    """复盘优化建议"""
    problem: str
    advice: str
    priority: str  # 高/中/低

@dataclass
class VideoData:
    """已发布视频数据"""
    play_count: int
    like_count: int
    comment_count: int
    stay_duration: float  # 平均停留时长（秒）
    finish_rate: float  # 完播率（0-1）

# ===================== 核心：四大智能 Agent =====================
class TopicAnalysisAgent:
    """选题分析 Agent：爬取热门数据 + 分析偏好 + 长链推理生成高潜力选题"""
    
    # 模拟平台热门词库（实际场景可替换为真实爬虫接口）
    PLATFORM_HOT_WORDS = {
        "知识科普": ["新手入门", "避坑", "干货总结", "一秒学会", "亲身实测"],
        "生活好物": ["平价好物", "提升幸福感", "懒人必备", "宿舍神器", "无限回购"],
        "职场成长": ["搞钱思路", "升职技巧", "职场禁忌", "效率提升", "副业推荐"],
        "美食教程": ["零失败", "5分钟搞定", "低成本", "外卖平替", "家常做法"]
    }

    def analyze(self, account_type: str) -> List[Topic]:
        print(f"\n【选题分析 Agent】正在分析【{account_type}】赛道热门数据...")
        time.sleep(1)
        
        # 长链推理步骤 1：获取赛道热门词
        hot_words = self.PLATFORM_HOT_WORDS.get(account_type, self.PLATFORM_HOT_WORDS["生活好物"])
        
        # 长链推理步骤 2：模拟用户偏好建模（基于热门词互动率）
        topics = []
        for i in range(random.randint(3, 5)):
            word = random.choice(hot_words)
            # 长链推理步骤 3：生成高潜力选题并评估
            topic = Topic(
                title=f"{account_type}：{word}，90%的人不知道",
                audience=f"关注{account_type}的18-35岁用户，喜欢实用、快速获取价值",
                advantage=f"包含热门词【{word}】，预计用户停留率提升40%",
                heat_score=random.randint(7, 10)
            )
            topics.append(topic)
        
        print(f"✅ 选题分析完成，生成{len(topics)}个高潜力选题")
        return topics


class ScriptGenerateAgent:
    """脚本生成 Agent：结合平台算法偏好（3秒抓眼球+节奏节点）生成分镜脚本"""
    
    def generate(self, topic: Topic) -> List[ScriptNode]:
        print(f"\n【脚本生成 Agent】正在为选题生成脚本：{topic.title}")
        time.sleep(1)
        
        # 遵循短视频黄金算法结构：3秒钩子 → 核心内容 → 价值总结 → 引导互动
        script = [
            ScriptNode(time="0-3s", scene="特写镜头", lines=f"{topic.title.split('：')[1]}！千万别划走！"),
            ScriptNode(time="3-10s", scene="讲解镜头", lines=f"今天给大家分享{topic.title.split('：')[0]}干货，专门针对{topic.audience}设计"),
            ScriptNode(time="10-25s", scene="演示镜头", lines=f"{topic.advantage}，看完你就能直接用，少走弯路"),
            ScriptNode(time="25-30s", scene="总结镜头", lines="觉得有用点赞关注，下期继续分享！评论区扣1发完整版资料")
        ]
        print("✅ 脚本生成完成（符合平台算法：3秒抓眼球+节奏节点优化）")
        return script


class MaterialMatchAgent:
    """素材匹配 Agent：关键词匹配 + 商用素材推荐 + 标题/互动文案生成"""
    
    def match(self, script: List[ScriptNode], topic_title: str) -> Dict:
        print(f"\n【素材匹配 Agent】正在匹配商用素材与文案...")
        time.sleep(1)
        
        # 步骤 1：提取脚本核心关键词
        key_words = topic_title.split("：")[1] if "：" in topic_title else topic_title
        
        # 步骤 2：推荐可商用素材（实际场景可对接素材库 API）
        materials = [
            Material(type="视频素材", content=f"{key_words}相关实拍片段（可商用）"),
            Material(type="背景音乐", content="轻快Vlog背景音乐（无版权）"),
            Material(type="封面图片", content=f"{key_words}大字突出封面（可商用）")
        ]
        
        # 步骤 3：生成平台爆款标题 + 评论区互动文案
        titles = [
            f"绝了！{key_words}，建议收藏！",
            f"{key_words}，90%的人都忽略了！",
            f"后悔没早知道：{key_words}"
        ]
        
        comments = [
            "大家觉得有用吗？评论区告诉我～",
            "需要完整版资料的扣1，我发你",
            "下期想看什么内容？留言点菜"
        ]
        
        result = {
            "materials": materials,
            "titles": titles,
            "comments": comments
        }
        print("✅ 素材&文案匹配完成（全部可商用）")
        return result


class ReviewOptimizeAgent:
    """复盘优化 Agent：分析发布数据 + 定位转化问题 + 长链推理生成优化建议"""
    
    def review(self, video_data: VideoData) -> List[OptimizeAdvice]:
        print(f"\n【复盘优化 Agent】正在分析视频数据...")
        time.sleep(1)
        
        advice_list = []
        
        # 长链推理步骤 1：基于数据定位问题节点
        if video_data.stay_duration < 3:
            # 长链推理步骤 2：分析原因并生成高优先级建议
            advice_list.append(OptimizeAdvice(
                problem="开头停留率极低（平均停留时长不足3秒）",
                advice="建议替换开场方式，使用更夸张的视觉冲击或直接抛出痛点问题",
                priority="高"
            ))
        
        if video_data.finish_rate < 0.3:
            advice_list.append(OptimizeAdvice(
                problem="完播率偏低（低于30%）",
                advice="建议压缩核心内容时长，或在中间增加1-2个小反转/提问保持观众注意力",
                priority="高"
            ))
        
        if video_data.like_count / video_data.play_count < 0.03:
            advice_list.append(OptimizeAdvice(
                problem="点赞率偏低（低于3%）",
                advice="建议在结尾明确引导点赞，或增加‘点赞保存’的心理暗示",
                priority="中"
            ))
        
        if video_data.comment_count / video_data.play_count < 0.01:
            advice_list.append(OptimizeAdvice(
                problem="评论率偏低（低于1%）",
                advice="建议在评论区置顶互动话题，或在视频中抛出开放式问题",
                priority="中"
            ))
        
        if not advice_list:
            advice_list.append(OptimizeAdvice(
                problem="数据表现良好",
                advice="建议基于当前选题方向继续创作，可尝试扩展相关子话题",
                priority="低"
            ))
        
        print("✅ 复盘分析完成，形成闭环优化建议")
        return advice_list

# ===================== 主程序：多 Agent 协作流程演示 =====================
def main():
    print("="*60)
    print("🚀 短视频脚本 + 内容运营 Agent 系统启动")
    print("="*60)
    
    # 1. 用户输入：账号定位
    account_type = input("请输入账号定位/赛道（如：知识科普/生活好物/职场成长/美食教程）：")
    
    # 2. 选题分析 Agent 生成选题
    topic_agent = TopicAnalysisAgent()
    topics = topic_agent.analyze(account_type)
    
    # 展示选题并让用户选择
    print("\n📋 生成的高潜力选题：")
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic.title}（热度评分：{topic.heat_score}/10）")
        print(f"   受众：{topic.audience}")
        print(f"   优势：{topic.advantage}\n")
    
    selected_idx = int(input("请选择要创作的选题编号：")) - 1
    selected_topic = topics[selected_idx]
    
    # 3. 脚本生成 Agent 生成分镜脚本
    script_agent = ScriptGenerateAgent()
    script = script_agent.generate(selected_topic)
    
    print("\n🎬 生成的分镜脚本：")
    for node in script:
        print(f"[{node.time}] {node.scene}：{node.lines}")
    
    # 4. 素材匹配 Agent 推荐素材与文案
    material_agent = MaterialMatchAgent()
    material_result = material_agent.match(script, selected_topic.title)
    
    print("\n🎨 推荐的可商用素材：")
    for mat in material_result["materials"]:
        print(f"- {mat.type}：{mat.content}")
    
    print("\n📝 推荐的爆款标题：")
    for title in material_result["titles"]:
        print(f"- {title}")
    
    print("\n💬 推荐的评论区互动文案：")
    for comment in material_result["comments"]:
        print(f"- {comment}")
    
    # 5. 模拟视频发布后，复盘优化 Agent 进行分析
    print("\n" + "="*60)
    print("📊 模拟视频发布后的数据复盘环节")
    print("="*60)
    
    # 模拟输入发布数据（实际场景可对接平台数据 API）
    video_data = VideoData(
        play_count=int(input("请输入播放量：")),
        like_count=int(input("请输入点赞量：")),
        comment_count=int(input("请输入评论量：")),
        stay_duration=float(input("请输入平均停留时长（秒）：")),
        finish_rate=float(input("请输入完播率（0-1之间的小数）："))
    )
    
    # 复盘优化
    review_agent = ReviewOptimizeAgent()
    advice_list = review_agent.review(video_data)
    
    print("\n🔧 复盘优化建议：")
    for advice in advice_list:
        print(f"【{advice.priority}优先级】")
        print(f"问题：{advice.problem}")
        print(f"建议：{advice.advice}\n")
    
    print("="*60)
    print("✨ 全流程演示结束，形成创作闭环迭代")
    print("="*60)

if __name__ == "__main__":
    main()
