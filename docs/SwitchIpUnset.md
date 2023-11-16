# SwitchIpUnset

The distributed virtual switch received a reconfiguration request to activate a feature that requires a switch IP address.  However, the IP address for the switch has not been specified.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.switch_ip_unset import SwitchIpUnset

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchIpUnset from a JSON string
switch_ip_unset_instance = SwitchIpUnset.from_json(json)
# print the JSON string representation of the object
print SwitchIpUnset.to_json()

# convert the object into a dict
switch_ip_unset_dict = switch_ip_unset_instance.to_dict()
# create an instance of SwitchIpUnset from a dict
switch_ip_unset_form_dict = switch_ip_unset.from_dict(switch_ip_unset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


