# UpdateIpPoolRequestType

The parameters of *IpPoolManager.UpdateIpPool*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dc** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**pool** | [**IpPool**](IpPool.md) |  | 

## Example

```python
from vmware_vi.models.update_ip_pool_request_type import UpdateIpPoolRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIpPoolRequestType from a JSON string
update_ip_pool_request_type_instance = UpdateIpPoolRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateIpPoolRequestType.to_json()

# convert the object into a dict
update_ip_pool_request_type_dict = update_ip_pool_request_type_instance.to_dict()
# create an instance of UpdateIpPoolRequestType from a dict
update_ip_pool_request_type_form_dict = update_ip_pool_request_type.from_dict(update_ip_pool_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


