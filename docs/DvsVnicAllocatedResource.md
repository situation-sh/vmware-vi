# DvsVnicAllocatedResource

This class defines the allocated resource information on a virtual NIC  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vnic_key** | **str** | The virtual NIC key  ***Since:*** vSphere API 6.0  | 
**reservation** | **int** | The reservation specification on the virtual NIC.  Units in Mbits/s  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_vnic_allocated_resource import DvsVnicAllocatedResource

# TODO update the JSON string below
json = "{}"
# create an instance of DvsVnicAllocatedResource from a JSON string
dvs_vnic_allocated_resource_instance = DvsVnicAllocatedResource.from_json(json)
# print the JSON string representation of the object
print DvsVnicAllocatedResource.to_json()

# convert the object into a dict
dvs_vnic_allocated_resource_dict = dvs_vnic_allocated_resource_instance.to_dict()
# create an instance of DvsVnicAllocatedResource from a dict
dvs_vnic_allocated_resource_form_dict = dvs_vnic_allocated_resource.from_dict(dvs_vnic_allocated_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


