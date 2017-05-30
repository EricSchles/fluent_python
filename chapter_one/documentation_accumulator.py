import os
import collections

Code = collections.namedtuple(
    'Code',
    [
        'filename',
        'docstring_present',
        'docstring_percent',
        'comment_percent'
    ]
)


class CodeClimate:
    def __init__(self, root_directory):
        self.code_objects = []
        code_files_counted = 0
        files_with_docs = 0
        doc_percent_per_file = 0
        comment_percent_per_file = 0
        for dir_name, subdir_list, file_list in os.walk(root_directory):
            for filename in file_list:
                if filename.endswith(".py"):
                    code_files_counted += 1
                    code = self._read_file(filename)
                    tmp = self._analyze(code)
                    self.code_objects.append(
                        Code(
                            filename,
                            tmp["docs_present"],
                            tmp["docs_percent"],
                            tmp["comment_percent"]
                        )
                    )
                    if tmp["docs_present"]:
                        files_with_docs += 1
                        doc_percent_per_file += tmp["docs_percent"]
                    comment_percent_per_file += tmp["comment_percent"]
        self.overall_code_climate = Code(
            'overall_code_climate',
            files_with_docs/float(code_files_counted),
            doc_percent_per_file/float(code_files_counted),
            comment_percent_per_file/float(code_files_counted)
        )

    def _read_file(self, filename):
        with open(os.path.abspath(filename), "r") as f:
            return f.read().split("\n")

    def _analyze(self, code):
        docs_present = self._look_for_docs(code)
        if docs_present:
            # a number between 0 and 1
            docs_percent = self._docs_calc_percentage(code)
        else:
            docs_percent = 0
        comment_percent = self._comment_percentage(code)
        return {
            "docs_present": docs_present,
            "docs_percent": docs_percent,
            "comment_percent": comment_percent
        }

    def _look_for_docs(self, code):
        for index, line in enumerate(code):
            if "class" in line or "def" in line:
                next_line = code[index+1].strip()
                if next_line.startswith('"""') or next_line.startswith('"'):
                    return True
                if next_line.startswith("'''") or next_line.startswith("'"):
                    return True
        return False

    def _docs_calc_percentage(self, code):
        count_objs_with_docs = 0
        count_of_total_objs = 0
        for index, line in enumerate(code):
            if "class" in line or "def" in line:
                count_of_total_objs += 1
                next_line = code[index+1].strip()
                if next_line.startswith('"""') or next_line.startswith('"'):
                    count_objs_with_docs += 1
                if next_line.startswith("'''") or next_line.startswith("'"):
                    count_objs_with_docs += 1
        return count_objs_with_docs / float(count_of_total_objs)

    def _comment_percentage(self, code):
        comment_count = 0
        for line in code:
            if "#" in line:
                comment_count += 1
        return float(comment_count) / len(code)

    def __len__(self):
        return len(self.code_objects)

    def __getitem__(self, position):
        return self.code_objects[position]
