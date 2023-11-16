# ArrayOfSendSNMPAction

A boxed array of *SendSNMPAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SendSNMPAction]**](SendSNMPAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_send_snmp_action import ArrayOfSendSNMPAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSendSNMPAction from a JSON string
array_of_send_snmp_action_instance = ArrayOfSendSNMPAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfSendSNMPAction.to_json()

# convert the object into a dict
array_of_send_snmp_action_dict = array_of_send_snmp_action_instance.to_dict()
# create an instance of ArrayOfSendSNMPAction from a dict
array_of_send_snmp_action_form_dict = array_of_send_snmp_action.from_dict(array_of_send_snmp_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


