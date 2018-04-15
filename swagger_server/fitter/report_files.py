# checks if a is of type t
def check_type(x, t):
    assert type(x) == t
    return x


# checks if a is of one of the types in lt
def check_types(x, lt):
    assert type(x) in lt
    return x


# checks if x is in opts
def check_enum(x, opts):
    assert x in opts
    return x


# checks if a is an array of element type t
def check_array(a, t):
    for it in a:
        assert type(it]) == t
    return check_type(a, list)


def FileRef:
    def __init__(self, **kwargs):
        self.id = None
        self.path = None
        if 'id' in kwargs:
            self.id = check_type(kwargs['id'], str)
        elif 'path' in kwargs:
            self.path = check_type(kwargs['path'], str)
        else:
            raise Exception("unspecified file reference")

    def get_info(self):
        if self.id is not None:
            return {
                'id': self.id
            }
        elif self.path is not None:
            return {
                'path': self.path
            }
        else:
            raise Exception("unspecified file reference")


def make_report(**kwargs):
    return {
        'title': check_type(kwargs['title'], str),
        'description': check_type(kwargs['description'], str),
        'created': check_type(kwargs['created'], str),
        'blocks': check_type(kwargs['blocks'], list)
    }


# blocks: [dict]
def make_vert_block(blocks):
    return {
        'type': 'vertical',
        'blocks': check_array(blocks, dict)
    }


# blocks: [dict]
def make_horizontal_block(blocks):
    return {
        'type': 'horizontal',
        'blocks': check_array(blocks, dict)
    }


# blocks: [dict]
# weights: [int]
def make_weighted_block(blocks, weights):
    assert len(blocks) == len(weights)
    return {
        'type': 'weighted',
        'blocks': [
            {
                'weight': check_type(weights[i], int),
                'blocks': check_type(blocks[i], dict)
            } for i in range(len(blocks))
        ]
    }


class TextHTMLInfo:
    # ! contents: string
    def __init__(self, **kwargs):
        self.contents = check_type(kwargs['contents'], str)

    def get_info(self):
        return {
            'type': 'html',
            'contents': self.contents
        }


class TextRefInfo:
    # ! to: string
    # text: string
    def __init__(self, **kwargs):
        self.to = check_type(kwargs['to'], str)
        self.text = None
        if 'text' in kwargs:
            self.text = check_type(kwargs['text'], str)

    def get_info(self):
        b = {
            'type': 'ref',
            'to': self.to
        }
        if self.text is not None:
            b['text'] = self.text
        return b


class TextFileRefInfo:
    # ! to: string
    # text: string
    def __init__(self, **kwargs):
        self.to = check_type(kwargs['to'], FileRef)
        self.text = None
        if 'text' in kwargs:
            self.text = check_type(kwargs['text'], str)

    def get_info(self):
        b = {
            'type': 'ref',
            'to': self.to.get_info()
        }
        if self.text is not None:
            b['text'] = self.text
        return b


def make_text_block(text_fname, **kwargs):
    b = {
        'type': 'text',
        'paragraphs': [
            {
                'contents': check_types(info, [TextHTMLInfo,
                                               TextRefInfo,
                                               TextFileRefInfo]).get_info()
            }
            for info in kwargs['text_infos']
        ]
    }
    if 'id' in kwargs:
        b['id'] = check_type(kwargs['id'], str)
    if 'title': in kwargs:
        b['title'] = check_type(kwargs['title'], str)
    if 'subtitle' in kwargs:
        b['subtitle'] = check_type(kwargs['subtitle'], str)
    if 'caption' in kwargs:
        b['caption'] = check_type(kwargs['caption'], str)


# ! file: file_ref
# id: string
# title: string
# sub_title: string
# caption: string
# columns: [int]
# is_subset_of: string
# rank_column: int
# max_rows: int
def make_table_block(table_fname, **kwargs):
    b = {
        'type': 'table',
        'file': check_type(table_fname, FileRef).get_info()
    }
    if 'id' in kwargs:  # string
        b['id'] = check_type(kwargs['id'], str)
    if 'title' in kwargs:  # string
        b['title'] = check_type(kwargs['title'], str)
    if 'sub_title' in kwargs:  # string
        b['sub_title'] = check_type(kwargs['subtitle'], str)
    if 'caption' in kwargs:  # string
        b['caption'] = check_type(kwargs['caption'], str)
    if 'columns' in kwargs:  # [integer]
        b['columns'] = check_array(kwargs['columns'], int)
    if 'is_subset_of' in kwargs:  # file_ref
        b['is_subset_of'] = check_type(kwargs['is_subset_of'], FileRef).get_info()
    if 'rank_column' in kwargs:  # integer
        b['rank_column'] = check_type(kwargs['rank_column'], int)
    return b


class PlotInformation:
    LINE, SCATTER, PIE = range(3)
    # ! type: <LINE, SCATTER, PIE>
    # ! file: file_ref
    # ! x_col: int
    # ! y_col: int
    # legend_name: string
    # is_subset_of: string
    # error_max_col: int
    # error_min_col: int
    # x_axis:
    #   x_start_hint:  number
    #   x_end_hint: number
    #   x_label: string
    # y_axis:
    #   y_start_hint:  number
    #   y_end_hint: number
    #   y_label: string
    def __init__(self, **kwargs):
        plt_type = check_type(kwargs['type'], str)
        if plt_type == PlotInformation.LINE:
            self.plt_type = 'line'
        elif plt_type == PlotInformation.SCATTER:
            self.plt_type = 'scatter'
        elif plt_type = PlotInformation.PIE:
            self.plt_type = 'pie'
        self.plt_type = check_type(self.plt_type, str)
        self.file = check_type(kwargs['file'], FileRef)
        self.x_col = check_type(kwargs['x_col'], int)
        self.y_col = check_type(kwargs['y_col'], int)
        self.legend_name = None
        self.is_subset_of = None
        self.error_max_col = None
        self.error_min_col = None
        if 'legend_name' in kwargs:
            self.set_legend_name(kwargs['legend_name'])
        if 'is_subset_of' in kwargs:
            self.set_is_subset_of(kwargs['is_subset_of'])
        if 'error_max_col' in kwargs:
            self.error_max_col = check_type(kwargs['error_max_col'], int)
        if 'error_min_col' in kwargs:
            self.error_min_col = check_type(kwargs['error_min_col'], int)

        self.x_start_hint = None
        self.x_end_hint = None
        self.x_label = None
        if 'x_start_hint' in kwargs:
            self.x_start_hint = check_types(kwargs['x_end_hint'], [int, float])
        if 'x_end_hint' in kwargs:
            self.x_end_hint = check_types(kwargs['x_end_hint'], [int, float])
        if 'x_label' in kwargs:
            self.x_label = check_type(kwargs['x_label'], str)

        self.y_start_hint = None
        self.y_end_hint = None
        self.y_label = None
        if 'y_start_hint' in kwargs:
            self.y_start_hint = check_types(kwargs['y_end_hint'], [int, float])
        if 'y_end_hint' in kwargs:
            self.y_end_hint = check_types(kwargs['y_end_hint'], [int, float])
        if 'y_label' in kwargs:
            self.y_label = check_type(kwargs['y_label'], str)


    def set_legend_name(self, legend_name):
        self.legend_name = check_type(legend_name, str)

    def set_is_subset_of(self, legend_name)
        self.is_subset_of = check_type(kwargs['is_subset_of'], FileRef)

    def set_error_cols(self, error_max_col, error_min_col):
        self.error_max_col = check_type(error_max_col, int)
        self.error_min_col = check_type(error_min_col, int)

    def get_data_info():
        info = {
            'type': self.plt_type,
            'file': self.file.get_info(),
            'x_col': self.x_col,
            'y_col': self.y_col
        }
        if self.legend_name is not None:
            info['legend_name'] = self.legend_name
        if self.is_subset_of is not None:
            info['is_subset_of'] = self.is_subset_of.get_info()
        if self.error_max_col is not None:
            info['error_max_col'] = self.error_max_col
        if self.error_min_col is not None:
            info['error_min_col'] = self.error_min_col
        return info

    def get_x_axis_info():
        info = {
        }
        if self.x_start_hint is not None:
            info['start_hint'] = self.x_start_hint
        if self.x_end_hint is not None:
            info['end_hint'] = self.x_end_hint
        if self.x_label is not None:
            info['label'] = self.x_label
        return info

    def get_y_axis_info():
        info = {
        }
        if self.y_start_hint is not None:
            info['start_hint'] = self.y_start_hint
        if self.y_end_hint is not None:
            info['end_hint'] = self.y_end_hint
        if self.y_label is not None:
            info['label'] = self.y_label
        return info


# id: string
# title: string
# sub_title: string
# caption: string
# display_legend: string
# plot_infos: [ PlotInformation ]
def make_plot_block(**kwargs):
    b = {
        'type': 'plot',
        'data_series': check_list([p.get_data_info()
                                   for p in kwargs['plot_infos']], dict),
        'x_axis': check_list([p.get_x_axis_info()
                              for p in kwargs['plot_infos']], dict),
        'x_axis': check_list([p.get_y_axis_info()
                              for p in kwargs['plot_infos']], dict)
    }
    if 'id' in kwargs:
        b['id'] = check_type(kwargs['id'], str)
    if 'title' in kwargs:
        b['title'] = check_type(kwargs['title'], str)
    if 'sub_title' in kwargs:
        b['sub_title'] = check_type(kwargs['sub_title'], str)
    if 'caption' in kwargs:
        b['caption'] = check_type(kwargs['caption'], str)
    if 'display_legend' in kwargs:
        b['display_legend'] = check_type(kwargs['display_legend'], str)
    return b


# id: string
# title: string
# sub_title: string
# caption: string
# ! file: file_ref
# ! file_type: <png, svg>
def make_image_block(image_fname, **kwargs):
    b = {
        'type': 'image',
        'file': check_type(kwargs['file'], FileRef).get_info(),
        'file_type': check_enum(check_type(kwargs['file_type'], str),
                                ['png, 'svg])
    }
    if 'id' in kwargs:
        b['id'] = check_type(kwargs['id'], str)
    if 'title' in kwargs:
        b['title'] = check_type(kwargs['title'], str)
    if 'sub_title' in kwargs:
        b['sub_title'] = check_type(kwargs['subtitle'], str)
    if 'caption' in kwargs:
        b['caption'] = check_type(kwargs['caption'], str)
    return b
