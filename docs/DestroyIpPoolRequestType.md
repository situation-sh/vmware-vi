# DestroyIpPoolRequestType

The parameters of *IpPoolManager.DestroyIpPool*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dc** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**id** | **int** | The unique ID of the pool  | 
**force** | **bool** | If true, the pool will be destroyed even if it is in use  | 

## Example

```python
from vmware_vi.models.destroy_ip_pool_request_type import DestroyIpPoolRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DestroyIpPoolRequestType from a JSON string
destroy_ip_pool_request_type_instance = DestroyIpPoolRequestType.from_json(json)
# print the JSON string representation of the object
print DestroyIpPoolRequestType.to_json()

# convert the object into a dict
destroy_ip_pool_request_type_dict = destroy_ip_pool_request_type_instance.to_dict()
# create an instance of DestroyIpPoolRequestType from a dict
destroy_ip_pool_request_type_form_dict = destroy_ip_pool_request_type.from_dict(destroy_ip_pool_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


