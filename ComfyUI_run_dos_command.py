import subprocess
import os
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import server
else:
    server = None


class RunDOSCommand:
    def __init__(self):
        # 初始化方法，可用于设置初始状态
        self.reset()

    def reset(self):
        # 重置节点状态的方法
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "additional_text": ("STRING", {"default": ""}),
                "command": ("STRING", {"default": "dir"})                
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "run_command"
    CATEGORY = "utils"

    def run_command(self, command, additional_text):
        try:
            # 执行命令并捕获输出
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                output = result.stdout
            else:
                output = result.stderr
            # 拼接额外文本和命令输出
            output = f"Additional Text: {additional_text}\nCommand Output: {output}"
        except Exception as e:
            # 处理异常
            output = str(e)
        return (output,)


NODE_CLASS_MAPPINGS = {
    "RunDOSCommand": RunDOSCommand
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RunDOSCommand": "Run DOS Command",
   
} 
    