# OvfCreateImportSpecParams

Parameters for deploying an OVF.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_name** | **str** | The name to set on the entity (more precisely, on the top-level vApp or VM of the entity) as it appears in VI.  If empty, the product name is obtained from the ProductSection of the descriptor. If that name is not specified, the ovf:id of the top-level entity is used.  ***Since:*** vSphere API 4.0  | 
**host_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**network_mapping** | [**List[OvfNetworkMapping]**](OvfNetworkMapping.md) | The mapping of network identifiers from the descriptor to networks in the VI infrastructure.  The privilege Network.Assign is required on all networks in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**ip_allocation_policy** | **str** | The IP allocation policy chosen by the caller.  See *VAppIPAssignmentInfo*.  ***Since:*** vSphere API 4.0  | [optional] 
**ip_protocol** | **str** | The IP protocol chosen by the caller.  See *VAppIPAssignmentInfo*.  ***Since:*** vSphere API 4.0  | [optional] 
**property_mapping** | [**List[KeyValue]**](KeyValue.md) | The assignment of values to the properties found in the descriptor.  If no value is specified for an option, the default value from the descriptor is used.  ***Since:*** vSphere API 4.0  | [optional] 
**resource_mapping** | [**List[OvfResourceMap]**](OvfResourceMap.md) | Deprecated as of vSphere API 5.1.  The resource configuration for the created vApp.  This can be used to distribute a vApp across multiple resource pools (and create linked children).  ***Since:*** vSphere API 4.1  | [optional] 
**disk_provisioning** | **str** | An optional disk provisioning.  If set, all the disks in the deployed OVF will have get the same specified disk type (e.g., thin provisioned). The valide values for disk provisioning are: - *monolithicSparse* - *monolithicFlat* - *twoGbMaxExtentSparse* - *twoGbMaxExtentFlat* - *thin* - *thick* - *sparse* - *flat* - *seSparse*    See also *VirtualDiskMode_enum*.  ***Since:*** vSphere API 4.1  | [optional] 
**instantiation_ost** | [**OvfConsumerOstNode**](OvfConsumerOstNode.md) |  | [optional] 

## Example

```python
from vmware_vi.models.ovf_create_import_spec_params import OvfCreateImportSpecParams

# TODO update the JSON string below
json = "{}"
# create an instance of OvfCreateImportSpecParams from a JSON string
ovf_create_import_spec_params_instance = OvfCreateImportSpecParams.from_json(json)
# print the JSON string representation of the object
print OvfCreateImportSpecParams.to_json()

# convert the object into a dict
ovf_create_import_spec_params_dict = ovf_create_import_spec_params_instance.to_dict()
# create an instance of OvfCreateImportSpecParams from a dict
ovf_create_import_spec_params_form_dict = ovf_create_import_spec_params.from_dict(ovf_create_import_spec_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


