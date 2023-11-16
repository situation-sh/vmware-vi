# CreateResourcePoolRequestType

The parameters of *ResourcePool.CreateResourcePool*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ResourcePool. Any % (percent) character used in this parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this parameter.  | 
**spec** | [**ResourceConfigSpec**](ResourceConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_resource_pool_request_type import CreateResourcePoolRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourcePoolRequestType from a JSON string
create_resource_pool_request_type_instance = CreateResourcePoolRequestType.from_json(json)
# print the JSON string representation of the object
print CreateResourcePoolRequestType.to_json()

# convert the object into a dict
create_resource_pool_request_type_dict = create_resource_pool_request_type_instance.to_dict()
# create an instance of CreateResourcePoolRequestType from a dict
create_resource_pool_request_type_form_dict = create_resource_pool_request_type.from_dict(create_resource_pool_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


