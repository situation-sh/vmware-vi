# DvsFault

Base class for faults that can be thrown while invoking a distributed virtual switch operation.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_fault import DvsFault

# TODO update the JSON string below
json = "{}"
# create an instance of DvsFault from a JSON string
dvs_fault_instance = DvsFault.from_json(json)
# print the JSON string representation of the object
print DvsFault.to_json()

# convert the object into a dict
dvs_fault_dict = dvs_fault_instance.to_dict()
# create an instance of DvsFault from a dict
dvs_fault_form_dict = dvs_fault.from_dict(dvs_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


