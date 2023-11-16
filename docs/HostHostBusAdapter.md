# HostHostBusAdapter

This data object type describes the bus adapter for the host.  A host bus adapter (HBA) is a hardware or software adapter that connects the host to storage devices. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The linkable identifier.  | [optional] 
**device** | **str** | The device name of host bus adapter.  | 
**bus** | **int** | The host bus number.  | 
**status** | **str** | The operational status of the adapter.  Valid values include \&quot;online\&quot;, \&quot;offline\&quot;, \&quot;unbound\&quot;, and \&quot;unknown\&quot;.  | 
**model** | **str** | The model name of the host bus adapter.  | 
**driver** | **str** | The name of the driver.  | [optional] 
**pci** | **str** | The Peripheral Connect Interface (PCI) ID of the device representing the host bus adapter.  | [optional] 
**storage_protocol** | **str** | The type of protocol supported by the host bus adapter.  The list of supported values is described in *HostStorageProtocol_enum*. When unset, a default value of \&quot;scsi\&quot; is assumed.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_host_bus_adapter import HostHostBusAdapter

# TODO update the JSON string below
json = "{}"
# create an instance of HostHostBusAdapter from a JSON string
host_host_bus_adapter_instance = HostHostBusAdapter.from_json(json)
# print the JSON string representation of the object
print HostHostBusAdapter.to_json()

# convert the object into a dict
host_host_bus_adapter_dict = host_host_bus_adapter_instance.to_dict()
# create an instance of HostHostBusAdapter from a dict
host_host_bus_adapter_form_dict = host_host_bus_adapter.from_dict(host_host_bus_adapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


