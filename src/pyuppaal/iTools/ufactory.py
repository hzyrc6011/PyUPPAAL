from typing import List, Tuple, Dict
import xml.etree.cElementTree as ET


class UFactory:
    """
    usage: UppaalFactory.function(xxx)
    用户一般不直接调用这个class
    用来生产UPPAAL里的xml element组件，主要包含
    declaration, (简单字符串)
    query, (简单字符串)
    queries, (多个queries)
    location,
    transition,
    template,
    """

    @staticmethod
    def declaration(declaration: str):
        """
        构造UPPAAL的declaration
        declaration: str, declaration里的全部内容
        """
        dec_elem = ET.Element('declaration')
        dec_elem.text = declaration
        return dec_elem

    @staticmethod
    def __query(query: str):
        """
        query: str, 验证语句
        构造一个query
        query示例：
            <query>
                <formula>E&lt;&gt; Output.pass</formula>
                <comment />
            </query>
        """
        query_elem = ET.Element('query')

        # 构建并添加formula
        formula_elem = ET.Element('formula')
        formula_elem.text = query
        query_elem.append(formula_elem)

        # 构建并添加comment
        query_elem.append(ET.Element('comment'))
        return query_elem

    @staticmethod
    def queries(queries: List[str]):
        """
        queries: List[str], 多条验证语句
        完整queries示例
        <queries>
            <query>
                <formula>E&lt;&gt; Output.pass</formula>
                <comment />
            </query>
            <query>
                <formula>E&lt;&gt; Output2.pass</formula>
                <comment />
            </query>
        </queries>
        """
        queries_elem = ET.Element('queries')
        # 构建并加入多个queries element
        for query in queries:
            queries_elem.append(UppaalFactory.__query(query))
        return queries_elem

    @staticmethod
    def location(location_id: int, pos_x: int, pos_y: int,
                 inv: str = None, name: str = None, is_committed: bool = False):
        """
        构造一个location
        id: int, location的id，注意不要和以前的location的id重复
        pos_x, pos_y: int, location的位置
        inv: str, location的invariant，比如'gclk<=10'或者'gclk<100'
        name: str, location的名字，默认是None
        is_committed: bool, 是否为committed，默认不是committed

        完整location示例：
            <location id="id37" x="-169" y="-59">
                <name x="90" y="166">pass</name>
                <label kind="invariant" x="-212" y="-42">gclk&lt;=122</label>
                <committed/>
            </location>
        """
        location = ET.Element('location', {'id': f'id{location_id}',
                                           'x': str(pos_x),
                                           'y': str(pos_y)})
        # 添加名字
        if name is not None:
            location_name = ET.Element('name', {'x': str(pos_x),
                                                'y': str(pos_y - 20)})
            location_name.text = name
            location.append(location_name)
        # 添加inv
        if inv is not None:
            label = ET.Element('label', {'kind': 'invariant',
                                         'x': str(pos_x),
                                         'y': str(pos_y - 40)})
            label.text = inv
            location.append(label)
        # 添加committed
        if is_committed:
            location.append(ET.Element('committed'))
        return location

    @staticmethod
    def transition(sourceID: int, targetID: int, pos_x: int, pos_y: int,
                   guard: str = None, sync: str = None, clock_reset: str = None):
        """
        sourceID: int, 起点id
        targetID: int, 终点id
        post_x, post_y: int, 符号的位置
        guard: str, edge的guard，如't>=10', 't>100'
        sync: str, synchronisation信号，需要注明!或者？
        clock_reset: str, 如't=0'
        完整transition示例：
        <transition>
            <source ref="id7"/>
            <target ref="id6"/>
            <label kind="guard" x="139" y="90">t&gt;=tERPMin</label>
            <label kind="synchronisation" x="123" y="90">sync?</label>
            <label kind="assignment" x="156" y="107">t=0</label>
        </transition>
        """
        transition = ET.Element('transition')
        # 构建并添加source
        source = ET.Element('source', {'ref': f'id{sourceID}'})
        transition.append(source)
        # 构建并添加target
        target = ET.Element('target', {'ref': f'id{targetID}'})
        transition.append(target)
        # 构建并添加guard
        if guard is not None:
            label_guard = ET.Element('label', {'kind': 'guard',
                                               'x': str(pos_x),
                                               'y': str(pos_y)})
            label_guard.text = guard
            transition.append(label_guard)
        # 构建并添加synchronisation
        if sync is not None:
            label_sync = ET.Element('label', {'kind': 'synchronisation',
                                              'x': str(pos_x),
                                              'y': str(pos_y - 30)})
            label_sync.text = sync
            transition.append(label_sync)
        # 构建并添加assignment
        if clock_reset is not None:
            label_assignment = ET.Element('label', {'kind': 'assignment',
                                                    'x': str(pos_x),
                                                    'y': str(pos_y - 60)})
            label_assignment.text = clock_reset
            transition.append(label_assignment)
        return transition

    @staticmethod
    def template(name: str, locations: List[ET.Element], init_id: int, transitions: List[ET.Element],
                 parameter: str = None, declaration: str = None):
        """
        name: str, template的名字
        locations: List[ET.Element], 由UppaalFactory.construct_location()构造出的一系列locations
        init_id: int, initial location的id，比如47
        transitions: List[ET.Element], 由UppaalFactory.construct_transition()构造出的一系列transitions
        parameter: str,
            比如：<parameter>broadcast chan &amp;actNode, actPath,int tERPMin, int tERPMax</parameter>
        declaration: str,
            比如: <declaration>clock t;</declaration>
        构建一个新的template
        一个template的基本框架为：
            <template>
                <name>NodeN</name>
                可以没有<parameter>broadcast chan &amp;actNode, int tERPMin, int tERPMax</parameter>
                可以没有<declaration>clock t;</declaration>

                <location> </location>
                <location> </location>
                <location> </location>
                <init ref="id47"/>
                <transition> </transition>
                <transition> </transition>
                <transition> </transition>
            </template>
        """
        template = ET.Element('template')
        # 创建并加入name
        name_elem = ET.Element('name')
        name_elem.text = name
        template.append(name_elem)

        # 创建并加入parameter
        if parameter is not None:
            parameter_elem = ET.Element('parameter')
            parameter_elem.text = parameter
            template.append(parameter_elem)

        # 创建并加入declaration
        if declaration is not None:
            declaration_elem = ET.Element('declaration')
            declaration_elem.text = parameter
            template.append(declaration_elem)

        # 加入locations
        for location in locations:
            template.append(location)

        # 创建并加入init
        init_elem = ET.Element('init', {'ref': f'id{init_id}'})
        template.append(init_elem)

        # 加入 transitions
        for transition in transitions:
            template.append(transition)
        return template

    @staticmethod
    def input(input_signals: List[Tuple[str, str, str]], init_id: int, input_name: str = 'Input'):
        """
        构建输入的线性模型，类似monitor
        """
        pass

    @staticmethod
    def monitor(monitor_name: str, signals: List[Tuple[str, str, str]], init_id: int, strict: bool = False):
        """
        构建新的线性monitor
        monitor_name: string
        signals: List[Tuple[str, int, int]],
                 每个tuple分别对应[signal, guard, inv]
                 signal, guard, inv, name 都可以是None
                 signal: 信号名称, 需要带上?
                 guard: str, 比如gclk>=10
                 inv: str, 比如gclk<=5
                 注意：在连接的时候是按照信号在list出现的顺序连接的
        init_id: int, 用来设置Monitor中最小的<init ref='xxx'/>
        strict: bool, 是否是严格观测。如果strict是True，则要求在给定观测之外禁止有其他观测。
        附：一个Monitor的基本框架为：
            <template>
                <name>Monitor</name>
                <location> </location>
                <init ref="id47"/>
                <transition> </transition>
            </template>
        """
        # 创建locations
        locations = []
        for i in range(len(signals)):
            # [signal, guard, inv, name]
            location = UppaalFactory.location(init_id + i, 300 * i, 200, signals[i][2])
            locations.append(location)
        # 需要多一个尾巴location
        location = UppaalFactory.location(init_id + len(signals), 300 * len(signals), 200, name='pass')
        locations.append(location)

        # 创建transitions
        transitions = []
        for i in range(len(signals)):
            # [signal, guard, inv]
            transition = UppaalFactory.transition(init_id + i, init_id + i + 1, i * 300 + 100, 200,
                                                  signals[i][1], signals[i][0])
            transitions.append(transition)

        # # 如果是strict，需要创建一个fail location，并且构建对应transitions边指向fail
        # if strict:
        #     # 构建一个fail location
        #     fail_location_id = init_id + len(signals) + 1
        #     # 注意inv是最后的
        #     location = UppaalFactory.location(fail_location_id, 300 * len(signals) // 2, -200, inv=signals[-1][2],
        #                                       name='fail')
        #     locations.append(location)
        #
        #     # 构建指向fail的transitions
        #     for i in range(len(signals)):
        #         # 指向fail，注意guard是小于等于
        #         transition = UppaalFactory.transition(init_id + i, fail_location_id, i * 300 + 100, -200,
        #                                               signals[i][1].replace('>=', '<'), signals[i][0])
        #         transitions.append(transition)

        # 如果是strict，需要给每个location创建fail location，并且构建对应transitions边指向对应的fail location
        if strict:
            # 构建指向fail的transitions
            for i in range(len(signals)):
                # 构建一个fail location
                fail_location_id = init_id + len(signals) + i + 1
                # 注意inv是对应的编号
                location = UppaalFactory.location(fail_location_id, 300 * i, -200, inv=signals[i][2].replace('<=', '<'),
                                                  name='fail' + str(i))
                locations.append(location)

                # 指向fail，注意guard是大于
                if i == 0:
                    transition = UppaalFactory.transition(init_id + i, fail_location_id, i * 300 + 100, -100,
                                                          None, signals[i][0])
                else:
                    transition = UppaalFactory.transition(init_id + i, fail_location_id, i * 300 + 100, -100,
                                                          signals[i - 1][1].replace('>=', '>'), signals[i][0])

                transitions.append(transition)

        monitor_elem = UppaalFactory.template(monitor_name, locations, init_id, transitions)
        return monitor_elem

    @staticmethod
    def strict_monitor(monitor_name: str, signals: List[Tuple[str, str, str]], init_id: int):
        """
        构建新的线性monitor，并且要求在给定观测之外禁止有其他观测
        该函数调用了UppaalFactory.monitor()，让strict = True
        monitor_name: string
        signals: List[Tuple[str, int, int]],
                 每个tuple分别对应[signal, guard, inv]
                 signal, guard, inv, name 都可以是None
                 signal: 信号名称, 需要带上?
                 guard: str, 比如gclk>=10
                 inv: str, 比如gclk<=5
                 注意：在连接的时候是按照信号在list出现的顺序连接的
        init_id: int, 用来设置Monitor中最小的<init ref='xxx'/>
        """
        return UppaalFactory.monitor(monitor_name, signals, init_id, strict=True)

    @staticmethod
    def monitor_allpatterns(monitor_name: str, signals: List[Tuple[str, str, str]], init_id: int, edge_signal_dict: Dict[str, str]):
        """
        构建新的线性monitor
        monitor_name: string
        signals: List[Tuple[str, int, int]],
                 每个tuple分别对应[signal, guard, inv]
                 signal, guard, inv, name 都可以是None
                 signal: 信号名称, 需要带上?
                 guard: str, 比如gclk>=10
                 inv: str, 比如gclk<=5
                 注意：在连接的时候是按照信号在list出现的顺序连接的
        init_id: int, 用来设置Monitor中最小的<init ref='xxx'/>
        strict: bool, 是否是严格观测。如果strict是True，则要求在给定观测之外禁止有其他观测。
        附：一个Monitor的基本框架为：
            <template>
                <name>Monitor</name>
                <location> </location>
                <init ref="id47"/>
                <transition> </transition>
            </template>
        """
        # 创建locations
        locations = []
        for i in range(len(signals)):
            # [signal, guard, inv, name]
            location = UppaalFactory.location(init_id + i, 300 * i, 200, None)
            locations.append(location)
        # 需要多一个尾巴location
        location = UppaalFactory.location(init_id + len(signals), 300 * len(signals), 200, name='pass')
        locations.append(location)

        # 创建非法locations
        for i in range(len(signals)):
            j = 0
            for value in edge_signal_dict.values():
                if signals[i][0] != value.replace('!', '?'):
                    # [signal, guard, inv, name]
                    location = UppaalFactory.location(init_id + len(signals) + 1 + i * (len(edge_signal_dict)-1) + j, 300 * i, 500 + 100 * j, None)
                    locations.append(location)
                    j += 1

        # 创建transitions
        transitions = []
        for i in range(len(signals)):
            # [signal, guard, inv]
            transition = UppaalFactory.transition(init_id + i, init_id + i + 1, i * 300 + 100, 200,
                                                  None, signals[i][0])
            transitions.append(transition)

        # 创建非法transitions
        for i in range(len(signals)):
            j = 0
            for value in edge_signal_dict.values():
                if signals[i][0] != value.replace('!', '?'):
                    # [signal, guard, inv]
                    transition = UppaalFactory.transition(init_id + i, init_id + len(signals) + 1 + i * (len(edge_signal_dict)-1) + j, i * 300 + 100, 200,
                                                          None, value.replace('!', '?'))
                    transitions.append(transition)
                    j += 1

        monitor_elem = UppaalFactory.template(monitor_name, locations, init_id, transitions)
        return monitor_elem

    @staticmethod
    def input(monitor_name: str, signals: List[Tuple[str, str, str]], init_id: int, strict: bool = False):
        """
        构建新的线性monitor
        monitor_name: string
        signals: List[Tuple[str, int, int]],
                 每个tuple分别对应[signal, guard, inv]
                 signal, guard, inv, name 都可以是None
                 signal: 信号名称, 需要带上?
                 guard: str, 比如gclk>=10
                 inv: str, 比如gclk<=5
                 注意：在连接的时候是按照信号在list出现的顺序连接的
        init_id: int, 用来设置Monitor中最小的<init ref='xxx'/>
        strict: bool, 是否是严格观测。如果strict是True，则要求在给定观测之外禁止有其他观测。
        附：一个Monitor的基本框架为：
            <template>
                <name>Monitor</name>
                <location> </location>
                <init ref="id47"/>
                <transition> </transition>
            </template>
        """
        # 创建locations
        locations = []
        for i in range(len(signals)):
            # [signal, guard, inv, name]
            location = UppaalFactory.location(init_id + i, 300 * i, 200, signals[i][2])
            locations.append(location)
        # 需要多一个尾巴location
        location = UppaalFactory.location(init_id + len(signals), 300 * len(signals), 200, name='Finish')
        locations.append(location)

        # 创建transitions
        transitions = []
        for i in range(len(signals)):
            # [signal, guard, inv]
            transition = UppaalFactory.transition(init_id + i, init_id + i + 1, i * 300 + 100, 200,
                                                  signals[i][1], signals[i][0])
            transitions.append(transition)

        # # 如果是strict，需要创建一个fail location，并且构建对应transitions边指向fail
        # if strict:
        #     # 构建一个fail location
        #     fail_location_id = init_id + len(signals) + 1
        #     # 注意inv是最后的
        #     location = UppaalFactory.location(fail_location_id, 300 * len(signals) // 2, -200, inv=signals[-1][2],
        #                                       name='fail')
        #     locations.append(location)
        #
        #     # 构建指向fail的transitions
        #     for i in range(len(signals)):
        #         # 指向fail，注意guard是小于等于
        #         transition = UppaalFactory.transition(init_id + i, fail_location_id, i * 300 + 100, -200,
        #                                               signals[i][1].replace('>=', '<'), signals[i][0])
        #         transitions.append(transition)

        # 如果是strict，需要给每个location创建fail location，并且构建对应transitions边指向对应的fail location
        if strict:
            # 构建指向fail的transitions
            for i in range(len(signals)):
                # 构建一个fail location
                fail_location_id = init_id + len(signals) + i + 1
                # 注意inv是对应的编号
                location = UppaalFactory.location(fail_location_id, 300 * i, -200, inv=signals[i][2].replace('<=', '<'),
                                                  name='fail' + str(i))
                locations.append(location)

                # 指向fail，注意guard是大于
                if i == 0:
                    transition = UppaalFactory.transition(init_id + i, fail_location_id, i * 300 + 100, -100,
                                                          None, None)
                else:
                    transition = UppaalFactory.transition(init_id + i, fail_location_id, i * 300 + 100, -100,
                                                          signals[i - 1][1].replace('>=', '>'), None)

                transitions.append(transition)

        monitor_elem = UppaalFactory.template(monitor_name, locations, init_id, transitions)
        return monitor_elem

    @staticmethod
    def signal_converter(signal_dict: Dict[str, str], init_id: int, converter_name: str = 'SignalConverter'):
        """
        将某些可观测信号转化成另一些信号
        signal_dict: Dict[str, str]，信号对应的字典
        init_id: int, location最小的id，防止location的冲突

        比如：signal_dict = {'actPathHisA': 'sigOut',
                            'actPathHisH': 'sigOut',
                            'actPathHisV': 'sigOut',
                            'sigIn': 'actNodeSA'}
        会构造出如xx图片的自动机
        """
        pass
