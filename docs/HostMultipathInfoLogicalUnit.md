# HostMultipathInfoLogicalUnit

The *HostMultipathInfoLogicalUnit* data object represents a storage entity that provides disk blocks to a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  | 
**id** | **str** | Identifier of LogicalUnit.  Use this id to configure LogicalUnit multipathing policy using *HostStorageSystem.SetMultipathLunPolicy*.  | 
**lun** | [**ScsiLun**](ScsiLun.md) |  | 
**path** | [**List[HostMultipathInfoPath]**](HostMultipathInfoPath.md) | Array of paths available to access this LogicalUnit.  | 
**policy** | [**HostMultipathInfoLogicalUnitPolicy**](HostMultipathInfoLogicalUnitPolicy.md) |  | 
**storage_array_type_policy** | [**HostMultipathInfoLogicalUnitStorageArrayTypePolicy**](HostMultipathInfoLogicalUnitStorageArrayTypePolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_multipath_info_logical_unit import HostMultipathInfoLogicalUnit

# TODO update the JSON string below
json = "{}"
# create an instance of HostMultipathInfoLogicalUnit from a JSON string
host_multipath_info_logical_unit_instance = HostMultipathInfoLogicalUnit.from_json(json)
# print the JSON string representation of the object
print HostMultipathInfoLogicalUnit.to_json()

# convert the object into a dict
host_multipath_info_logical_unit_dict = host_multipath_info_logical_unit_instance.to_dict()
# create an instance of HostMultipathInfoLogicalUnit from a dict
host_multipath_info_logical_unit_form_dict = host_multipath_info_logical_unit.from_dict(host_multipath_info_logical_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


