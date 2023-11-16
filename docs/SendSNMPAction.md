# SendSNMPAction

This data object type specifies an SNMP trap that is triggered by an alarm. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.send_snmp_action import SendSNMPAction

# TODO update the JSON string below
json = "{}"
# create an instance of SendSNMPAction from a JSON string
send_snmp_action_instance = SendSNMPAction.from_json(json)
# print the JSON string representation of the object
print SendSNMPAction.to_json()

# convert the object into a dict
send_snmp_action_dict = send_snmp_action_instance.to_dict()
# create an instance of SendSNMPAction from a dict
send_snmp_action_form_dict = send_snmp_action.from_dict(send_snmp_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


