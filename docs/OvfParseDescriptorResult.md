# OvfParseDescriptorResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eula** | **List[str]** | The list of all EULAs contained in the OVF  ***Since:*** vSphere API 4.0  | [optional] 
**network** | [**List[OvfNetworkInfo]**](OvfNetworkInfo.md) | The list of networks required by the OVF  ***Since:*** vSphere API 4.0  | [optional] 
**ip_allocation_scheme** | **List[str]** | The kind of IP allocation supported by the guest.  See *VAppIPAssignmentInfo*.  ***Since:*** vSphere API 4.0  | [optional] 
**ip_protocols** | **List[str]** | The IP protocols supported by the guest.  See *VAppIPAssignmentInfo*.  ***Since:*** vSphere API 4.0  | [optional] 
**var_property** | [**List[VAppPropertyInfo]**](VAppPropertyInfo.md) | Metadata about the properties contained in the OVF  ***Since:*** vSphere API 4.0  | [optional] 
**product_info** | [**VAppProductInfo**](VAppProductInfo.md) |  | [optional] 
**annotation** | **str** | The annotation info contained in the OVF  ***Since:*** vSphere API 4.0  | 
**approximate_download_size** | **int** | The OVF Manager&#39;s best guess as to the total amount of data that must be transferred to download the entity.  This may be inaccurate due to disk compression etc.  ***Since:*** vSphere API 4.0  | [optional] 
**approximate_flat_deployment_size** | **int** | The OVF Manager&#39;s best guess as to the total amount of space required to deploy the entity if using flat disks.  ***Since:*** vSphere API 4.0  | [optional] 
**approximate_sparse_deployment_size** | **int** | The OVF Manager&#39;s best guess as to the total amount of space required to deploy the entity using sparse disks.  ***Since:*** vSphere API 4.0  | [optional] 
**default_entity_name** | **str** | The default name to use for the entity, if a product name is not specified.  This is the ID of the OVF top-level entity, or taken from a ProductSection.  ***Since:*** vSphere API 4.0  | 
**virtual_app** | **bool** | True if the OVF contains a vApp (containing one or more vApps and/or virtual machines), as opposed to a single virtual machine.  ***Since:*** vSphere API 4.0  | 
**deployment_option** | [**List[OvfDeploymentOption]**](OvfDeploymentOption.md) | The list of possible deployment options.  ***Since:*** vSphere API 4.0  | [optional] 
**default_deployment_option** | **str** | The key of the default deployment option.  Empty only if there are no deployment options.  ***Since:*** vSphere API 4.0  | 
**entity_name** | [**List[KeyValue]**](KeyValue.md) | A list of the child entities contained in this package and their location in the vApp hierarchy.  Each entry is a (key,value) pair, where the key is the display name, and the value is a unique path identifier for the entity in the vApp. The path is constructed by appending the id of each entity of the path down to the entity, separated by slashes. For example, the path for a child of the root entity with id &#x3D; \&quot;vm1\&quot;, would simply be \&quot;vm1\&quot;. If the vm is the child of a VirtualSystemCollection called \&quot;webTier\&quot;, then the path would be \&quot;webTier/vm\&quot;.  ***Since:*** vSphere API 4.1  | [optional] 
**annotated_ost** | [**OvfConsumerOstNode**](OvfConsumerOstNode.md) |  | [optional] 
**error** | [**List[MethodFault]**](MethodFault.md) | Errors that happened during processing.  Something will be wrong with the result.  For example, during export, devices could be missing (in which case this array will contain one or more instances of Unsupported-/UnknownDevice).  ***Since:*** vSphere API 4.0  | [optional] 
**warning** | [**List[MethodFault]**](MethodFault.md) | Non-fatal warnings from the processing.  The result will be valid, but the user may choose to reject it based on these warnings.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.ovf_parse_descriptor_result import OvfParseDescriptorResult

# TODO update the JSON string below
json = "{}"
# create an instance of OvfParseDescriptorResult from a JSON string
ovf_parse_descriptor_result_instance = OvfParseDescriptorResult.from_json(json)
# print the JSON string representation of the object
print OvfParseDescriptorResult.to_json()

# convert the object into a dict
ovf_parse_descriptor_result_dict = ovf_parse_descriptor_result_instance.to_dict()
# create an instance of OvfParseDescriptorResult from a dict
ovf_parse_descriptor_result_form_dict = ovf_parse_descriptor_result.from_dict(ovf_parse_descriptor_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


