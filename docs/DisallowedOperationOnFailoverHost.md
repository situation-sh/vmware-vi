# DisallowedOperationOnFailoverHost

Fault thrown when an attempt is made to perform a disallowed operation on a host that has been configured as a failover host in an cluster that has High Availability enabled.  See *ClusterFailoverHostAdmissionControlPolicy*. Examples of such operations are destroying a host, moving a host out of a cluster, or powering on a virtual machine on a specific host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**hostname** | **str** | Name of the failover host.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.disallowed_operation_on_failover_host import DisallowedOperationOnFailoverHost

# TODO update the JSON string below
json = "{}"
# create an instance of DisallowedOperationOnFailoverHost from a JSON string
disallowed_operation_on_failover_host_instance = DisallowedOperationOnFailoverHost.from_json(json)
# print the JSON string representation of the object
print DisallowedOperationOnFailoverHost.to_json()

# convert the object into a dict
disallowed_operation_on_failover_host_dict = disallowed_operation_on_failover_host_instance.to_dict()
# create an instance of DisallowedOperationOnFailoverHost from a dict
disallowed_operation_on_failover_host_form_dict = disallowed_operation_on_failover_host.from_dict(disallowed_operation_on_failover_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


