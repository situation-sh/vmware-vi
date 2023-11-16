# ResourceNotAvailable

A ResourceNotAvailable fault indicating that some error has occurred because a resource was not available.  Information about the resource that is in use may be supplied.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_type** | **str** | Type of container that contains the resource.  ***Since:*** vSphere API 4.0  | [optional] 
**container_name** | **str** | Name of container that contains the resource.  .  ***Since:*** vSphere API 4.0  | [optional] 
**type** | **str** | Type of resource that is not available.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.resource_not_available import ResourceNotAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceNotAvailable from a JSON string
resource_not_available_instance = ResourceNotAvailable.from_json(json)
# print the JSON string representation of the object
print ResourceNotAvailable.to_json()

# convert the object into a dict
resource_not_available_dict = resource_not_available_instance.to_dict()
# create an instance of ResourceNotAvailable from a dict
resource_not_available_form_dict = resource_not_available.from_dict(resource_not_available_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


