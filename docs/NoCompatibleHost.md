# NoCompatibleHost

A NoCompatibleHost fault is thrown when DRS cannot find a compatible host in a given compute resource to run a virtual machine on.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The list of hosts that are not compatible, each element has a corresponding fault in the error array.  ***Since:*** vSphere API 4.0  Refers instances of *HostSystem*.  | [optional] 
**error** | [**List[MethodFault]**](MethodFault.md) | An error in this array indicates why the corresponding host in the host array is incompatible.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.no_compatible_host import NoCompatibleHost

# TODO update the JSON string below
json = "{}"
# create an instance of NoCompatibleHost from a JSON string
no_compatible_host_instance = NoCompatibleHost.from_json(json)
# print the JSON string representation of the object
print NoCompatibleHost.to_json()

# convert the object into a dict
no_compatible_host_dict = no_compatible_host_instance.to_dict()
# create an instance of NoCompatibleHost from a dict
no_compatible_host_form_dict = no_compatible_host.from_dict(no_compatible_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


