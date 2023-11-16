# ReplicationGroupId

The identity of a replication group.  A following well-known ReplicationGroupId  {  faultDomainId: <a validfaultdomainid>  deviceGroupId: ffffffff-ffff-ffff-ffff-ffffffffffff  }  means that VASA provider can create a new ReplicationGroupId on demand (this feature may not be supported in the first vSphere release that supports VVol replication).  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault_domain_id** | [**FaultDomainId**](FaultDomainId.md) |  | 
**device_group_id** | [**DeviceGroupId**](DeviceGroupId.md) |  | 

## Example

```python
from vmware_vi.models.replication_group_id import ReplicationGroupId

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationGroupId from a JSON string
replication_group_id_instance = ReplicationGroupId.from_json(json)
# print the JSON string representation of the object
print ReplicationGroupId.to_json()

# convert the object into a dict
replication_group_id_dict = replication_group_id_instance.to_dict()
# create an instance of ReplicationGroupId from a dict
replication_group_id_form_dict = replication_group_id.from_dict(replication_group_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


