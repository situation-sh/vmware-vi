# DestinationSwitchFull

For one of the networks that the virtual machine is using, the corresponding switch on the host is full.  If returned as part of migration checks, this is an error if either of the following is true, a warning otherwise: - The virtual ethernet card device backing is a distributed virtual switch - The virtual ethernet card device backing is a standard network and the   the device is connected 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.destination_switch_full import DestinationSwitchFull

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationSwitchFull from a JSON string
destination_switch_full_instance = DestinationSwitchFull.from_json(json)
# print the JSON string representation of the object
print DestinationSwitchFull.to_json()

# convert the object into a dict
destination_switch_full_dict = destination_switch_full_instance.to_dict()
# create an instance of DestinationSwitchFull from a dict
destination_switch_full_form_dict = destination_switch_full.from_dict(destination_switch_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


