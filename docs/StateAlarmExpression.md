# StateAlarmExpression

An alarm expression that uses the running state of either a virtual machine or a host as the condition that triggers the alarm.  Base type.  There are two alarm operands: yellow and red. At least one of them must be set. The value of the alarm expression is determined as follows: - If the red state is set but the yellow state is not: the expression is red when   the state operand matches (isEqual operator) or does not match (isUnequal operator)   the state of the managed entity. The expression is green otherwise. - If yellow is set but red is not: the expression is yellow when   the state operand matches (isEqual) or does not match (isUnequal)   the state of the managed entity. The expression is green otherwise. - If both yellow and red are set, the value of the expression is red when   the red state operand matches (isEqual) or does not match (isUnequal)   the state of the managed entity. Otherwise, the expression is   yellow when the yellow state operand matches (isEqual) or does not match (isUnequal)   the state of the managed entity. Otherwise, the expression is green. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**StateAlarmOperatorEnum**](StateAlarmOperatorEnum.md) |  | 
**type** | **str** | Name of the object type containing the property.  | 
**state_path** | **str** | Path of the state property.  The supported values: - for vim.VirtualMachine type: - runtime.powerState or summary.quickStats.guestHeartbeatStatus - for vim.HostSystem type: runtime.connectionState  | 
**yellow** | **str** | Whether or not to test for a yellow condition.  If this property is not set, do not calculate yellow status.  | [optional] 
**red** | **str** | Whether or not to test for a red condition.  If this property is not set, do not calculate red status.  | [optional] 

## Example

```python
from vmware_vi.models.state_alarm_expression import StateAlarmExpression

# TODO update the JSON string below
json = "{}"
# create an instance of StateAlarmExpression from a JSON string
state_alarm_expression_instance = StateAlarmExpression.from_json(json)
# print the JSON string representation of the object
print StateAlarmExpression.to_json()

# convert the object into a dict
state_alarm_expression_dict = state_alarm_expression_instance.to_dict()
# create an instance of StateAlarmExpression from a dict
state_alarm_expression_form_dict = state_alarm_expression.from_dict(state_alarm_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


