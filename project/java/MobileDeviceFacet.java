package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A mobile device facet is a grouping of characteristics unique to a portable computing device. [based on https://www.lexico.com/definition/mobile_device]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MobileDeviceFacet extends Facet {

  private String eSN;
  private List<String> iMEI;
  private String bluetoothDeviceName;
  private ZonedDateTime clockSetting;
  private String keypadUnlockCode;
  private Boolean mockLocationsAllowed;
  private String network;
  private ZonedDateTime phoneActivationTime;
  private Integer storageCapacityInBytes;


}