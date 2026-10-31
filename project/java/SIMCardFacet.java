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
  A SIM card facet is a grouping of characteristics unique to a subscriber identification module card intended to securely store the international mobile subscriber identity (IMSI) number and its related key, which are used to identify and authenticate subscribers on mobile telephony devices (such as mobile phones and computers). [based on https://en.wikipedia.org/wiki/SIM_card]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SIMCardFacet extends Facet {

  private String iCCID;
  private String iMSI;
  private String pIN;
  private String pUK;
  private String sIMForm;
  private String sIMType;
  private Identity carrier;
  private Integer storageCapacityInBytes;


}