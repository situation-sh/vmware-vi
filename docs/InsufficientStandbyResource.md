# InsufficientStandbyResource

This fault is thrown when Distributed Power Management cannot perform a given opeartion because there are insufficient CPU/memory resources on standby hosts (if any) to meet the requirements of the operation.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.insufficient_standby_resource import InsufficientStandbyResource

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientStandbyResource from a JSON string
insufficient_standby_resource_instance = InsufficientStandbyResource.from_json(json)
# print the JSON string representation of the object
print InsufficientStandbyResource.to_json()

# convert the object into a dict
insufficient_standby_resource_dict = insufficient_standby_resource_instance.to_dict()
# create an instance of InsufficientStandbyResource from a dict
insufficient_standby_resource_form_dict = insufficient_standby_resource.from_dict(insufficient_standby_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


