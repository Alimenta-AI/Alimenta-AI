import React, { useState, useContext } from "react";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { HiOutlineBars3 } from "react-icons/hi2";
import { CgLogIn } from "react-icons/cg";
import { GoSignIn } from "react-icons/go";
import { GoSignOut } from "react-icons/go";
import { BsPlusCircle } from "react-icons/bs";
import { BsPostageHeart } from "react-icons/bs";
import Box from "@mui/material/Box";
import Drawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import HomeIcon from "@mui/icons-material/Home";
import InfoIcon from "@mui/icons-material/Info";
import PhoneRoundedIcon from "@mui/icons-material/PhoneRounded";
import Logo from '../Assets/alimentaAi.png'
import { Link, useHistory } from 'react-router-dom'
import { AuthContext } from './AuthContext'

const Navbar = () => {
  const { isAuthenticated, handleLogout } = useContext(AuthContext);
  const [loggingOut, setLoggingOut] = useState(false);
  const history = useHistory();

  const handleLogoutClick = async () => {
    try {
      setLoggingOut(true);
      await handleLogout(); 
      setTimeout(() => {
        setLoggingOut(false); 
        history.push("/");
        toast.success("Logout concluído", {
          position: toast.POSITION.TOP_CENTER,
          autoClose: 3000,
        });
      }, 3000);
    } catch (error) {
      console.log(error);
      setLoggingOut(false);
      toast.error("Erro ao fazer logout", {
        position: toast.POSITION.TOP_CENTER,
        autoClose: 3000,
      });
    }
  };
  const [openMenu, setOpenMenu] = useState(false);
  const menuOptions = [
    {
      text: "Home",
      icon: <HomeIcon />,
      link: "/"
    },
    {
      text: "Sobre",
      icon: <InfoIcon />,
      link: "/sobre"
    }, 
    {
      text: "Adquira Já!",
      icon: <BsPlusCircle />,
      link: "/adquira"
    },
    {
      text: "Doe!",
      icon: <BsPostageHeart />,
      link: "/doe"
    },
    {
      text: "Contact",
      icon: <PhoneRoundedIcon />,
      link: "/contato"
    },
  ];
  
  if (isAuthenticated) {
    menuOptions.push({
      text: "Logout",
      icon: <GoSignOut />,
      link: "/",
      onClick: handleLogoutClick
    });
  } else {
    menuOptions.push(
      {
        text: "Cadastre-se",
        icon: <GoSignIn />,
        link: "/cadastro"
      },
      {
        text: "Login",
        icon: <CgLogIn />,
        link: "/login"
      }
    );
  }

  return (
    <>
    <ToastContainer/>
    <nav>
      <div className="nav-logo-container">
        <Link to="/"><img src={Logo} alt="Logo da Alimenta Ai" /></Link>
      </div>
      <div className="navbar-links-container">
        <ul className="list-container">
          <li className="nav-link"><Link to="/sobre">Sobre</Link></li>
          <li className="nav-link"><Link to="/adquira">Adquira Já!</Link></li>
          <li className="nav-link"><Link to="/doe">Doe!</Link></li>
          <li className="nav-link"><Link to="/contato">Contato</Link></li>
        </ul>
        {isAuthenticated ? (
          <button className="primary-button" onClick={handleLogoutClick}>Logout</button>
        ) : (
          <>
            <Link to="/cadastro"><button className="primary-button">Cadastre-se</button></Link>
            <Link to="/login"><button className="primary-button">Login</button></Link>
          </>
        )}
      </div>
      <div className="navbar-menu-container">
        <HiOutlineBars3 onClick={() => setOpenMenu(true)} />
      </div>
      <Drawer open={openMenu} onClose={() => setOpenMenu(false)} anchor="right">
        <Box
          sx={{ width: 250 }}
          role="presentation"
          onClick={() => setOpenMenu(false)}
          onKeyDown={() => setOpenMenu(false)}
        >
          <List>
            {menuOptions.map((item) => (
              <ListItem key={item.text} disablePadding>
                <ListItemButton component={Link} to={item.link} onClick={item.onClick}>
                  <ListItemIcon>{item.icon}</ListItemIcon>
                  <ListItemText primary={item.text} />
                </ListItemButton>
              </ListItem>
            ))}
            </List>
          <Divider />
        </Box>
      </Drawer>
    </nav>
    {loggingOut && (
        <div className="loading-overlay">
          <div className=""> Carregando...</div>
        </div>
      )}
    </>
  );
};

export default Navbar;
