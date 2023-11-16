# ArrayOfDatacenterEvent

A boxed array of *DatacenterEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatacenterEvent]**](DatacenterEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datacenter_event import ArrayOfDatacenterEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatacenterEvent from a JSON string
array_of_datacenter_event_instance = ArrayOfDatacenterEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatacenterEvent.to_json()

# convert the object into a dict
array_of_datacenter_event_dict = array_of_datacenter_event_instance.to_dict()
# create an instance of ArrayOfDatacenterEvent from a dict
array_of_datacenter_event_form_dict = array_of_datacenter_event.from_dict(array_of_datacenter_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


