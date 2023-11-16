# FilterInUse

A FilterInUse fault indicates that some error has occurred because an IO filter was in use.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | [**List[VirtualDiskId]**](VirtualDiskId.md) | Virtual disks that use the filter.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.filter_in_use import FilterInUse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterInUse from a JSON string
filter_in_use_instance = FilterInUse.from_json(json)
# print the JSON string representation of the object
print FilterInUse.to_json()

# convert the object into a dict
filter_in_use_dict = filter_in_use_instance.to_dict()
# create an instance of FilterInUse from a dict
filter_in_use_form_dict = filter_in_use.from_dict(filter_in_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


