package br.com.alimentaai.model;

public class ReservaCliente {
    private String dataReserva;
    private String checkIn;
    private String checkOut;
    private String reservaId;

    public ReservaCliente() {
    }

    public ReservaCliente(String dataReserva, String checkIn, String checkOut, String reservaId) {
        this.dataReserva = dataReserva;
        this.checkIn = checkIn;
        this.checkOut = checkOut;
        this.reservaId = reservaId;
    }

    public String getDataReserva() {
        return dataReserva;
    }

    public void setDataReserva(String dataReserva) {
        this.dataReserva = dataReserva;
    }

    public String getCheckIn() {
        return checkIn;
    }

    public void setCheckIn(String checkIn) {
        this.checkIn = checkIn;
    }

    public String getCheckOut() {
        return checkOut;
    }

    public void setCheckOut(String checkOut) {
        this.checkOut = checkOut;
    }

    public String getReservaId() {
        return reservaId;
    }

    public void setReservaId(String reservaId) {
        this.reservaId = reservaId;
    }

    @Override
    public String toString() {
        return "ReservaCliente{" +
                "dataReserva='" + dataReserva + '\'' +
                ", checkIn='" + checkIn + '\'' +
                ", checkOut='" + checkOut + '\'' +
                ", reservaId='" + reservaId + '\'' +
                '}';
    }
}
