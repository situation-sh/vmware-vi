# OvfFault

A common base type fault for all Ovf related faults.  The structure of OvfFault is as listed. - OvfFault   - OvfInvalidPackage     - OvfXmlFormat     - OvfWrongNamespace     - OvfElement       - OvfElementInvalidValue       - OvfUnexpectedElement       - OvfDuplicateElement       - OvfMissingElement       - OvfMissingElementNormalBoundary       - OvfDuplicatedElementBoundary     - OvfAttribute       - OvfMissingAttribute       - OvfInvalidValue         - OvfInvalidValueFormatMalformed         - OvfInvalidValueConfiguration         - OvfInvalidValueReference         - OvfInvalidValueEmpty     - OvfProperty       - OvfPropertyType       - OvfPropertyValue       - OvfPropertyNetwork       - OvfPropertyQualifier       - OvfPropertyQualifierWarning   - OvfConstraint     - OvfDiskOrderConstraint     - OvfHostResourceConstraint   - OvfUnsupportedPackage     - OvfNoHostNic     - OvfInvalidVmName     - OvfUnsupportedAttribute       - OvfUnsupportedAttributeValue     - OvfUnsupportedElement       - OvfUnsupportedElementValue       - OvfUnsupportedSection       - OvfNoSpaceOnController     - OvfUnsupportedType     - OvfUnsupportedSubType     - OvfHardwareCheck     - OvfNoSupportedHardwareFamily   - OvfExport     - OvfExportFailed     - OvfHardwareExport       - OvfUnsupportedDeviceExport       - OvfUnknownDeviceBacking       - OvfConnectedDevice         - OvfConnectedDeviceISO       - OvfUnableToExportDisk     - OvfPropertyExport     - OvfPropertyNetworkExport     - OvfDuplicatedPropertyIdExport   - OvfImport (these are typically returned as warnings)     - OvfImportFailed     - OvfHardwareCheck     - OvfMissingHardware     - OvfCpuCompatibility     - OvfCpuCompatibilityCheckNotSupported     - OvfUnsupportedDiskProvisioning     - OvfDuplicatedPropertyIdImport     - OvfNetworkMappingNotSupported   - OvfSystemFault     - OvfDiskMappingNotFound     - OvfHostValueNotParsed     - OvfInternalError     - OvfUnsupportedDeviceBackingOption     - OvfUnsupportedDeviceBackingInfo     - OvfToXmlUnsupportedElement     - OvfUnknownDevice     - OvfUnknownEntity   - OvfConsumerCallbackFault     - OvfConsumerFault     - OvfConsumerCommunicationError     - OvfConsumerInvalidSection     - OvfConsumerUndeclaredSection     - OvfConsumerUndefinedPrefix        All messages go into the vimlocale  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_fault import OvfFault

# TODO update the JSON string below
json = "{}"
# create an instance of OvfFault from a JSON string
ovf_fault_instance = OvfFault.from_json(json)
# print the JSON string representation of the object
print OvfFault.to_json()

# convert the object into a dict
ovf_fault_dict = ovf_fault_instance.to_dict()
# create an instance of OvfFault from a dict
ovf_fault_form_dict = ovf_fault.from_dict(ovf_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


