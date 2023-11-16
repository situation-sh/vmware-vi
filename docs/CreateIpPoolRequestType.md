# CreateIpPoolRequestType

The parameters of *IpPoolManager.CreateIpPool*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dc** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**pool** | [**IpPool**](IpPool.md) |  | 

## Example

```python
from vmware_vi.models.create_ip_pool_request_type import CreateIpPoolRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIpPoolRequestType from a JSON string
create_ip_pool_request_type_instance = CreateIpPoolRequestType.from_json(json)
# print the JSON string representation of the object
print CreateIpPoolRequestType.to_json()

# convert the object into a dict
create_ip_pool_request_type_dict = create_ip_pool_request_type_instance.to_dict()
# create an instance of CreateIpPoolRequestType from a dict
create_ip_pool_request_type_form_dict = create_ip_pool_request_type.from_dict(create_ip_pool_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


