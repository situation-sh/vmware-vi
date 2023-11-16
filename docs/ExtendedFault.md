# ExtendedFault

This fault is the container for faults logged by extensions.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault_type_id** | **str** | The id of the type of extended fault.  ***Since:*** VI API 2.5  | 
**data** | [**List[KeyValue]**](KeyValue.md) | Key/value pairs associated with fault.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.extended_fault import ExtendedFault

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedFault from a JSON string
extended_fault_instance = ExtendedFault.from_json(json)
# print the JSON string representation of the object
print ExtendedFault.to_json()

# convert the object into a dict
extended_fault_dict = extended_fault_instance.to_dict()
# create an instance of ExtendedFault from a dict
extended_fault_form_dict = extended_fault.from_dict(extended_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


