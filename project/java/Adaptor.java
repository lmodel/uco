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
  An adaptor is a device that physically converts the pin outputs but does not alter the underlying protocol (e.g. uSD to SD, CF to ATA, etc.)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Adaptor extends Device {



}