import sys

from niveristand import decorators, RealTimeSequence
from niveristand.datatypes import Boolean, Double, Int32, Int64
from niveristand.exceptions import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation
from testutilities.test_channels import TestChannels


a = 1
b = 2


@decorators.nivs_rt_sequence
def return_constant():
    a = Double(5)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_simple_numbers():
    a = Double(0)
    a.value = 1 ^ 3
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_num_nivsdatatype():
    a = Double(0)
    a.value = 1 ^ Double(3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype():
    a = Double(0)
    a.value = Double(1) ^ Double(3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype1():
    a = Double(0)
    a.value = Double(1) ^ Int32(3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype2():
    a = Boolean(0)
    a.value = Boolean(1) ^ Boolean(3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype3():
    a = Double(0)
    a.value = Int32(1) ^ Int32(3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_multiple_types():
    a = Int32(0)
    a.value = 1 ^ Int32(3) ^ 5
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_multiple_types1():
    a = Int64(1)
    a.value = 1 ^ Int64(5) ^ 3 ^ Int32(7)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_use_rtseq():
    a = Double(0)
    a.value = 1 ^ return_constant()
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_use_rtseq1():
    a = Double(0)
    a.value = return_constant() ^ 1
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_use_rtseq2():
    a = Double(0)
    a.value = Double(1) ^ return_constant()
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_use_rtseq3():
    a = Double(0)
    a.value = return_constant() ^ Double(1)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_use_rtseq4():
    a = Double(0)
    a.value = Int32(1) ^ return_constant()
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_use_rtseq5():
    a = Double(0)
    a.value = return_constant() ^ Int32(1)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_with_parantheses():
    a = Int32(0)
    a.value = 1 ^ (5 ^ 3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_with_parantheses1():
    a = Double(0)
    a.value = 1 ^ (Double(3) ^ Int32(5))
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_with_parantheses2():
    a = Double(0)
    a.value = Double(1) ^ (Int32(2) ^ 3.0) ^ Double(4)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_variables():
    a = Int32(5)
    b = Int32(0)
    b.value = 1 ^ a
    return b.value


@decorators.nivs_rt_sequence
def bitwise_xor_variables1():
    a = Int64(5)
    b = Int64(0)
    b.value = 1 ^ a.value
    return b.value


@decorators.nivs_rt_sequence
def bitwise_xor_variable_variable():
    a = Int32(1)
    b = Int64(3)
    c = Int32(0)
    c.value = a.value ^ b.value
    return c.value


@decorators.nivs_rt_sequence
def bitwise_xor_variable_variable1():
    a = Int32(1)
    b = Int64(3)
    c = Double(0)
    c.value = a.value ^ b.value
    return c.value


@decorators.nivs_rt_sequence
def bitwise_xor_variable_rtseq():
    a = Double(1)
    b = Double(0)
    b.value = a.value ^ return_constant()
    return b.value


@decorators.nivs_rt_sequence
def bitwise_xor_variable_rtseq1():
    a = Double(1)
    b = Double(0)
    b.value = return_constant() ^ a.value
    return b.value


@decorators.nivs_rt_sequence
def bitwise_xor_to_channelref():
    a = Double(0)
    a.value = 1 ^ Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_binary_unary():
    a = Int32(0)
    a.value = 3 ^ - 1
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_complex_expr():
    a = Double(0)
    a.value = 1 ^ (2 if 2 < 3 else 4)
    return a.value


# region augassign tests

@decorators.nivs_rt_sequence
def aug_bitwise_xor_simple_numbers():
    a = Int32(3)
    a.value ^= 7
    return a.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_num_nivsdatatype():
    a = Int32(1)
    a.value ^= Int32(3)
    return a.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_use_rtseq():
    a = Int32(1)
    a.value ^= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_with_parantheses():
    a = Int32(1)
    a.value ^= 7 ^ (5 ^ 3)
    return a.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_variables():
    a = Int32(7)
    b = Int32(3)
    b.value ^= a.value
    return b.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_to_channelref():
    a = Double(1)
    a.value ^= Double(TestChannels.HP_COUNT)
    return a.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_unary():
    a = Int32(3)
    a.value ^= -1
    return a.value


# end region augassign tests

# region invalid tests
@decorators.nivs_rt_sequence
def bitwise_xor_invalid_variables():
    return a.value ^ b


@decorators.nivs_rt_sequence
def bitwise_xor_invalid_variables1():
    return a.value ^ b.value


@decorators.nivs_rt_sequence
def bitwise_xor_invalid_variables2():
    a = Double(0)
    b = Double(0)
    b.value = a.value ^ 2
    return b


@decorators.nivs_rt_sequence
def bitwise_xor_to_None():
    a = Double(0)
    a.value = None ^ 1
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_invalid_rtseq_call():
    a = Double(0)
    a.value = return_constant ^ 1
    return a.value

# end region


run_tests = [
    (return_constant, (), 5.0),
    (bitwise_xor_simple_numbers, (), 2),
    (bitwise_xor_nivsdatatype_nivsdatatype3, (), 2),
    (bitwise_xor_variables, (), 4),
    (bitwise_xor_variables1, (), 4),
    (bitwise_xor_multiple_types, (), 7),
    (bitwise_xor_multiple_types1, (), 0),
    (bitwise_xor_with_parantheses, (), 7),
    (bitwise_xor_variable_variable, (), 2),
    (bitwise_xor_variable_variable1, (), 2),
    (bitwise_xor_binary_unary, (), -4),
    (aug_bitwise_xor_simple_numbers, (), 4),
    (aug_bitwise_xor_variables, (), 4),
    (aug_bitwise_xor_num_nivsdatatype, (), 2),
    (aug_bitwise_xor_with_parantheses, (), 0),
    (aug_bitwise_xor_unary, (), -4),
    (bitwise_xor_complex_expr, (), 3),
]

skip_tests = [
    (bitwise_xor_use_rtseq, (), "RTSeq call not implemented yet."),
    (bitwise_xor_use_rtseq1, (), "RTSeq call not implemented yet."),
    (bitwise_xor_use_rtseq2, (), "RTSeq call not implemented yet."),
    (bitwise_xor_use_rtseq3, (), "RTSeq call not implemented yet."),
    (bitwise_xor_use_rtseq4, (), "RTSeq call not implemented yet."),
    (bitwise_xor_use_rtseq5, (), "RTSeq call not implemented yet."),
    (bitwise_xor_variable_rtseq, (), "RTSeq call not implemented yet."),
    (bitwise_xor_variable_rtseq1, (), "RTSeq call not implemented yet."),
    (bitwise_xor_to_channelref, (), "Channel ref transform not yet implemented."),
    (bitwise_xor_invalid_variables2, (), "Attribute transformer doesn't catch the a.value.value problem."),
    (bitwise_xor_to_None, (), "Name transformer doesn't raise an exception for NoneType with python 2.7."),
    (bitwise_xor_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
    (aug_bitwise_xor_use_rtseq, (), "RTSeq call not implemented yet."),
    (aug_bitwise_xor_to_channelref, (), "Channel ref transform not yet implemented."),
]

fail_transform_tests = [
    (bitwise_xor_invalid_variables, (), TranslateError),
    (bitwise_xor_invalid_variables1, (), TranslateError),
    (bitwise_xor_num_nivsdatatype, (), VeristandError),
    (bitwise_xor_nivsdatatype_nivsdatatype, (), VeristandError),  # cannot do bitwise xor on Double
    (bitwise_xor_nivsdatatype_nivsdatatype1, (), VeristandError),  # cannot do bitwise xor on Double
    (bitwise_xor_nivsdatatype_nivsdatatype2, (), VeristandError),  # cannot do bitwise xor on Boolean
    (bitwise_xor_with_parantheses1, (), VeristandError),  # cannot do bitwise xor on Double
    (bitwise_xor_with_parantheses2, (), VeristandError),  # cannot do bitwise xor on Double
]


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    try:
        RealTimeSequence(func_name)
    except expected_result:
        pass
    except VeristandError as e:
        pytest.fail('Unexpected exception raised:' +
                    str(e.__class__) + ' while expected was: ' + expected_result.__name__)
    except Exception as exception:
        pytest.fail('ExpectedException not raised: ' + exception)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
