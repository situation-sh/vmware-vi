# Extension

This data object type contains all information about an extension.  An extension may contain zero or more server interfaces and zero or more clients.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Description**](Description.md) |  | 
**key** | **str** | Extension key.  Should follow java package naming conventions for uniqueness (e.g. \&quot;com.example.management\&quot;).  Extension names can only contain characters belonging to the lower ASCII character set (UTF-7) with the exception of the following characters: 1. All whitespace characters (\&quot;space\&quot; - ascii character 0x20 is allowed) 2. Control characters 3. Comma (ascii 0x2c), Forward slash (ascii 0x2f), Backward slash (ascii 0x5c),    Hash/Pound (ascii 0x23), Plus (ascii 0x2b), Greater (ascii 0x3e), Lesser (ascii 0x3c),    Equals (ascii 0x3d), Semi-colon (ascii 0x3b) and Double quote (ascii 0x22).     ***Since:*** VI API 2.5  | 
**company** | **str** | Company information.  ***Since:*** vSphere API 4.0  | [optional] 
**type** | **str** | Type of extension (example may include CP-DVS, NUOVA-DVS, etc.).  ***Since:*** vSphere API 4.0  | [optional] 
**version** | **str** | Extension version number as a dot-separated string.  For example, \&quot;1.0.0\&quot;  ***Since:*** VI API 2.5  | 
**subject_name** | **str** | Subject name from client certificate.  ***Since:*** VI API 2.5  | [optional] 
**server** | [**List[ExtensionServerInfo]**](ExtensionServerInfo.md) | Servers for this extension.  ***Since:*** VI API 2.5  | [optional] 
**client** | [**List[ExtensionClientInfo]**](ExtensionClientInfo.md) | Clients for this extension.  ***Since:*** VI API 2.5  | [optional] 
**task_list** | [**List[ExtensionTaskTypeInfo]**](ExtensionTaskTypeInfo.md) | Definitions of tasks defined by this extension.  ***Since:*** VI API 2.5  | [optional] 
**event_list** | [**List[ExtensionEventTypeInfo]**](ExtensionEventTypeInfo.md) | Definitions of events defined by this extension.  ***Since:*** VI API 2.5  | [optional] 
**fault_list** | [**List[ExtensionFaultTypeInfo]**](ExtensionFaultTypeInfo.md) | Definitions of faults defined by this extension.  ***Since:*** VI API 2.5  | [optional] 
**privilege_list** | [**List[ExtensionPrivilegeInfo]**](ExtensionPrivilegeInfo.md) | Definitions privileges defined by this extension.  ***Since:*** VI API 2.5  | [optional] 
**resource_list** | [**List[ExtensionResourceInfo]**](ExtensionResourceInfo.md) | Resource data for all locales  ***Since:*** VI API 2.5  | [optional] 
**last_heartbeat_time** | **datetime** | Last extension heartbeat time.  ***Since:*** VI API 2.5  | 
**health_info** | [**ExtensionHealthInfo**](ExtensionHealthInfo.md) |  | [optional] 
**ovf_consumer_info** | [**ExtensionOvfConsumerInfo**](ExtensionOvfConsumerInfo.md) |  | [optional] 
**extended_product_info** | [**ExtExtendedProductInfo**](ExtExtendedProductInfo.md) |  | [optional] 
**managed_entity_info** | [**List[ExtManagedEntityInfo]**](ExtManagedEntityInfo.md) | Information about entities managed by this extension.  An extension can register virtual machines as managed by itself, by setting the *managedBy* property of the virtual machine.  ***Since:*** vSphere API 5.0  | [optional] 
**shown_in_solution_manager** | **bool** | Opt-in to the Solution Manager.  If set to true, this extension will be shown in the Solution Manager. If not set, or set to false, this extension is not shown in the Solution Manager.  ***Since:*** vSphere API 5.0  | [optional] 
**solution_manager_info** | [**ExtSolutionManagerInfo**](ExtSolutionManagerInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.extension import Extension

# TODO update the JSON string below
json = "{}"
# create an instance of Extension from a JSON string
extension_instance = Extension.from_json(json)
# print the JSON string representation of the object
print Extension.to_json()

# convert the object into a dict
extension_dict = extension_instance.to_dict()
# create an instance of Extension from a dict
extension_form_dict = extension.from_dict(extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


