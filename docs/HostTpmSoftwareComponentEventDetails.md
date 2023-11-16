# HostTpmSoftwareComponentEventDetails

Details of a Trusted Platform Module (TPM) event recording a software component related event.  This event is created when measuring a software component installed on the system. A software component may be a tardisk, a kernel module or any other type supported by the package system.  Some software components are not packaged as VIBs (currently the package database and persistent state information of ESXi). For these components the VIB fields will contain empty strings.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_name** | **str** | Name of the software component that caused this TPM event.  ***Since:*** vSphere API 5.1  | 
**vib_name** | **str** | Name of the VIB containing the software component.  ***Since:*** vSphere API 5.1  | 
**vib_version** | **str** | Version of the VIB containing the software component.  ***Since:*** vSphere API 5.1  | 
**vib_vendor** | **str** | Vendor of the VIB containing the software component.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.host_tpm_software_component_event_details import HostTpmSoftwareComponentEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmSoftwareComponentEventDetails from a JSON string
host_tpm_software_component_event_details_instance = HostTpmSoftwareComponentEventDetails.from_json(json)
# print the JSON string representation of the object
print HostTpmSoftwareComponentEventDetails.to_json()

# convert the object into a dict
host_tpm_software_component_event_details_dict = host_tpm_software_component_event_details_instance.to_dict()
# create an instance of HostTpmSoftwareComponentEventDetails from a dict
host_tpm_software_component_event_details_form_dict = host_tpm_software_component_event_details.from_dict(host_tpm_software_component_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


