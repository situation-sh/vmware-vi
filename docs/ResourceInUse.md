# ResourceInUse

A ResourceInUse fault indicating that some error has occurred because a resource was in use.  Information about the resource that is in use may be supplied. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of resource that is in use.  | [optional] 
**name** | **str** | Name of the instance of the resource that is in use.  | [optional] 

## Example

```python
from vmware_vi.models.resource_in_use import ResourceInUse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceInUse from a JSON string
resource_in_use_instance = ResourceInUse.from_json(json)
# print the JSON string representation of the object
print ResourceInUse.to_json()

# convert the object into a dict
resource_in_use_dict = resource_in_use_instance.to_dict()
# create an instance of ResourceInUse from a dict
resource_in_use_form_dict = resource_in_use.from_dict(resource_in_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


