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
  A smartphone is a portable device that combines mobile telephone and computing functions into one unit. Examples include iPhone, Samsung Galaxy, Huawei, Blackberry. (Inferred by model and OperatingSystemFacet)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SmartPhone extends MobilePhone {



}