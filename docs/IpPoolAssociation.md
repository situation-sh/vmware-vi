# IpPoolAssociation

Information about a network or portgroup that is associated to an IP pool.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**network_name** | **str** | The name of the network or portgroup  This field is only used when querying existing IP pools. It is ignored when creating or updating pools.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ip_pool_association import IpPoolAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of IpPoolAssociation from a JSON string
ip_pool_association_instance = IpPoolAssociation.from_json(json)
# print the JSON string representation of the object
print IpPoolAssociation.to_json()

# convert the object into a dict
ip_pool_association_dict = ip_pool_association_instance.to_dict()
# create an instance of IpPoolAssociation from a dict
ip_pool_association_form_dict = ip_pool_association.from_dict(ip_pool_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


